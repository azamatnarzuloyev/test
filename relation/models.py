from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, HStoreField

class DaySavdoSell(models.Model):
    product_name = models.CharField(max_length=200)
    product_count = models.IntegerField(blank=True)


class Savdo(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True)
    daysavdo = models.ManyToManyField(DaySavdoSell, blank=True)

class Serene(models.Model):
    cod  =models.IntegerField()
    status = models.BooleanField(default=False, blank=True)


class SellerSerena(Serene):
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    delete = models.BooleanField(default=False, blank=True, null=True)


    

class Arraydjango(models.Model):
    serena = ArrayField(models.BigIntegerField(), blank=True)
    yosh = models.CharField(max_length=200, blank=True, null=True)


class HistoryField(models.Model):
    name = models.CharField(max_length=200, blank=True)
    code = HStoreField(blank=True, null=True)
