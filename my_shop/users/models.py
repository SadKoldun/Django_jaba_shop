from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Изображение пользователя')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

