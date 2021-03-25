from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class User(AbstractUser):
    bio = models.CharField('О себе', blank=True, null=True,)
    email = models.EmailField('Email', unique=True)
    role = models.CharField('Роль', choices=Roles.choices, default=Roles.USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        ordering = ('username',)
