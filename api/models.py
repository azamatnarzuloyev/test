from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)


class Material(models.Model):
    code = models.IntegerField()



class MeteraialProduct(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    material  = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True)


class SubCatogry(models.Model):
    count = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=200)
    supcategory = models.ManyToManyField(SubCatogry, blank=True)


