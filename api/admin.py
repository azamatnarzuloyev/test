from django.contrib import admin
from .models import Product, MeteraialProduct, Material, Category, SubCatogry

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(MeteraialProduct)
admin.site.register(Category)
admin.site.register(SubCatogry)
# Register your models here.
