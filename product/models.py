from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField('title', max_length=200)
    