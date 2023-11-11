from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class ShopSavdo(models.Model):
    product_name = models.CharField(max_length=200)
    product_count = models.IntegerField(blank=True, null=True)
    serene = ArrayField(models.BigIntegerField(), blank=True, null=True)
    material = models.BigIntegerField(blank=True, null=True)


class ShopName(models.Model):
    shop_name = models.CharField(max_length=200, blank=True)
    shop_status = models.BooleanField(default=False, blank=True)


class Shop(models.Model):
    name = models.CharField(max_length=200, blank=True)
    vendor = models.BooleanField(default=False, blank=True)
    yaratish =  models.BooleanField(default=False, blank=True)
    savdo_count = models.BigIntegerField(blank=True, null=True)
    savdo = models.ManyToManyField(ShopSavdo, blank=True)
    shop_name = models.ForeignKey(ShopName, on_delete=models.CASCADE , blank=True, null=True)




      
    

