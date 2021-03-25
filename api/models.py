from django.contrib.auth.models import AbstractUser
from django.db import models


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


class Title(models.Model):
    pass


class Review(models.Model):
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
        help_text='Дата отзыва'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='titles',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Произведение'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        str_return = str(self.text)[:15]
        return str_return


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name='комментарий'
    )

    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарий'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    created = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
