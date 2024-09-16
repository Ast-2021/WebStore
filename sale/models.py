from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    phone = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title