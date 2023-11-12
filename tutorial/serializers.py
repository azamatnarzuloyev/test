from rest_framework import serializers
from .models import Shop, ShopName, ShopSavdo


class ShopSerializers(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Shop
        fields = "__all__"

   

class Shopnameserializers(serializers.ModelSerializer):
    sed = serializers.IntegerField(read_only=True)
    code  = serializers.IntegerField(read_only=True)
    class Meta:
        model = ShopName
        fields ="__all__"



    

 
    

  


    


 
