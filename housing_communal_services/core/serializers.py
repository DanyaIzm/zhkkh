from rest_framework import serializers
from .models import *


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"


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


class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = "__all__"
