from rest_framework.routers import SimpleRouter
from .views import *


core_router = SimpleRouter()

core_router.register("houses", HouseViewSet)
core_router.register("flats", FlatViewSet)
core_router.register("tarifftypes", TariffTypeViewSet)
core_router.register("tariffs", TariffViewSet)
core_router.register("meters", MeterViewSet)
core_router.register("meterreadings", MeterReadingViewSet)


urlpatterns = core_router.urls
