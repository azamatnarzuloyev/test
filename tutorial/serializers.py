from rest_framework import serializers
from .models import Shop, ShopName, ShopSavdo


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"
    


 