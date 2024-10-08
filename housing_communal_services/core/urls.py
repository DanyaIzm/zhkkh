from rest_framework.routers import DefaultRouter
from .views import *


core_router = DefaultRouter()

core_router.register("houses", HouseViewSet)
core_router.register("flats", FlatViewSet)
core_router.register("tarifftypes", TariffTypeViewSet)
core_router.register("tariffs", TariffViewSet)
core_router.register("meters", MeterViewSet)
core_router.register("meterreadings", MeterReadingViewSet)


urlpatterns = core_router.urls