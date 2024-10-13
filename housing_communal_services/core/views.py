from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.


@extend_schema(tags=["Core Api"])
class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


@extend_schema(tags=["Core Api"])
class FlatViewSet(ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


@extend_schema(tags=["Core Api"])
class TariffTypeViewSet(ModelViewSet):
    queryset = TariffType.objects.all()
    serializer_class = TariffTypeSerializer


@extend_schema(tags=["Core Api"])
class TariffViewSet(ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


@extend_schema(tags=["Core Api"])
class MeterViewSet(ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


@extend_schema(tags=["Core Api"])
class MeterReadingViewSet(ModelViewSet):
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer
