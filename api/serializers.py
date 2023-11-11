from rest_framework import serializers
from .models import Product, MeteraialProduct

class Productmaterial(serializers.ModelSerializer):
    material_code = serializers.ReadOnlyField(source="material.code")
    product_name = serializers.ReadOnlyField(source="product.name")
    product = serializers.ReadOnlyField(source="product.id")
    class Meta:
        model = MeteraialProduct
        fields = ["id","count","product","material","material_code","product_name"]


class ProductSerialasers(serializers.ModelSerializer):
    product_material = Productmaterial( many=True, source="meteraialproduct_set")
    class Meta:
        model = Product
        fields = "__all__"


    def create(self, validated_data):
        meteraialproduct_set = validated_data.pop("meteraialproduct_set")
        new_product = Product.objects.create(**validated_data)
        for prod_material_data in meteraialproduct_set:
            MeteraialProduct.objects.create(
                product=new_product,
                material = prod_material_data.get('material'),
                count = prod_material_data.get('count')

            )

        return new_product



