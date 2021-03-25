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


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('slug',)
