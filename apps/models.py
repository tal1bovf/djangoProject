from django.db import models
from datetime import datetime


class Product(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='product_image')
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='post_image')
    description = models.TextField()
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductCommentary(models.Model):
    description = models.TextField(max_length=500)
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class PostCommentary(models.Model):
    description = models.TextField(max_length=500)
    post = models.ForeignKey('apps.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
