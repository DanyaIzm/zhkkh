from django.contrib import admin
from .models import *


admin.site.site_header = "Администрирование ЖКХ"

admin.site.register(House)
admin.site.register(Flat)
admin.site.register(TariffType)
admin.site.register(Tariff)
admin.site.register(Meter)
admin.site.register(MeterReading)
