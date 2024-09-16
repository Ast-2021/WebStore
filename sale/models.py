from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    phone = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title