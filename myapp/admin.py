from django.contrib import admin
from django.db import connection
from .models import Group, Person, Membership, Category, Subcategory, TestModel, ModelTest

admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(TestModel)
admin.site.register(ModelTest)



