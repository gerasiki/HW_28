from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=35)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=25)
