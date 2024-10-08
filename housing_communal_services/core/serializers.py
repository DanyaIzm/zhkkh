from rest_framework import serializers
from .models import *

class TariffTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffType
        fields = "__all__"


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = "__all__"


class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = "__all__"


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    flats = FlatSerializer(many=True, read_only=True)
    
    class Meta:
        model = House
        fields = "__all__"


class MeterReadingSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        try:
            return super().save(**kwargs)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
    
    class Meta:
        model = MeterReading
        fields = "__all__"
