from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# Create your views here.

class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class FlatViewSet(ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class TariffTypeViewSet(ModelViewSet):
    queryset = TariffType.objects.all()
    serializer_class = TariffTypeSerializer


class TariffViewSet(ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class MeterViewSet(ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


class MeterReadingViewSet(ModelViewSet):
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer
