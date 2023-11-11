from django.db import models
import uuid

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    invite_reason = models.CharField(max_length=64)
  
# class Code(models.Model):


# class Crmproduct(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.ManyToManyField(Code, blank=True, verbose_name='Code tavar')


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)




class Subcategory(Category):
    title = models.CharField(max_length=200)



class TestModel(models.Model):
    uuidField = models.UUIDField( default=uuid.uuid4, editable=False, auto_created=True)
    name = models.CharField(max_length=200, blank=True, null=True)



class ModelTest(TestModel):
    son = models.CharField(max_length=200)
    


    




