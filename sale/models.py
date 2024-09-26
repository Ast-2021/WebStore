from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    price = models.IntegerField(default=0)
    phone_regex = RegexValidator(regex=r'^\+?7?\d{11}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



    