from rest_framework import serializers
from .models import Person, Group, Membership, ModelTest


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class MemBerSerializers(serializers.ModelSerializer):
    person = PersonSerializers(read_only=True)
    class Meta:
        model = Membership
        fields = "__all__"

class GroupSerializers(serializers.ModelSerializer):
    member = MemBerSerializers(many=True, source='membership_set')
    # person = PersonSerializers(read_only=True)
    class Meta:
        model = Group
        fields = "__all__"


class ModelTestSeralizers(serializers.ModelSerializer):
    class Meta:
        model= ModelTest
        fields = "__all__"







