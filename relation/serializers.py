from rest_framework import serializers
from .models import Savdo, DaySavdoSell, Arraydjango, HistoryField


class SavdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savdo
        fields = "__all__"


class DaysavdoSerializers(serializers.ModelSerializer):

    class Meta:
        model = DaySavdoSell
        fields = ["id", 'product_name', "product_count"]



class Arraydjangoserializer(serializers.ModelSerializer):

    error_code = serializers.ListField()
    leng = serializers.IntegerField(read_only=True)
    class Meta:
        model = Arraydjango
        fields = "__all__"
        




class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoryField
        fields = "__all__"


    
    
    





