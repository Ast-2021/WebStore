from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', null=True, verbose_name='Фотография', default='users/standard_avatar.png')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')



    