from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    FIO = models.CharField(max_length=100, verbose_name='ФИО', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    comment = models.CharField(max_length=150, verbose_name='комментарий', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
