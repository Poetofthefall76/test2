from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    city = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user}"


class Category(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class Tags(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Product, related_name="tags")
