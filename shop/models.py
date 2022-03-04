from ctypes.wintypes import CHAR
from distutils.command.upload import upload
from random import choice
from telnetlib import STATUS
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['name']

class Brand(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


class Product(models.Model):
    STATUS_CHOICES = (
        ('NONE', 'NONE'),
        ('NEW', 'NEW'),
        ('SALE', 'SALE'),
        ('HOT', 'HOT'),
    )
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    short_description = RichTextField()
    tags = TaggableManager()
    description = RichTextField()
    specification = RichTextField()
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stack = models.IntegerField(default=5)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='NONE')
    is_fetured  = models.BooleanField(default=False)
    is_special  = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class ProductImages(models.Model):
    category = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')