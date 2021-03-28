from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg


class Roles(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class User(AbstractUser):
    bio = models.TextField('О себе', blank=True, null=True, )
    email = models.EmailField('Email', unique=True)
    role = models.CharField('Роль', max_length=10, choices=Roles.choices,
                            default=Roles.USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        ordering = ('username',)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('slug',)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('slug',)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        db_index=False,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        blank=True,
    )

    class Meta:
        ordering = ('id',)


class Review(models.Model):
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка', choices=[(r, r) for r in range(1, 11)],
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
        help_text='Дата отзыва',
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.score_avg = Review.objects.filter(title_id=self.title).aggregate(
            Avg('score')
        )
        self.title.rating = self.score_avg['score__avg']
        self.title.save()


class Comment(models.Model):

    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарий'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        'Дата',
        auto_now_add=True
    )

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='комментарий'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
