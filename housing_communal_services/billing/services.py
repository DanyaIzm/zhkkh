from django.db.models import Prefetch
from core.models import *
from .models import *


def generate_billing_report(
    month: int, year: int, house_id: int, billing_report_id: int
) -> None:
    flats = Flat.objects.filter(house_id=house_id).prefetch_related(
        Prefetch(
            "meters__readings",
            queryset=MeterReading.objects.filter(month=month, year=year),
        )
    )

    area_tariff = Tariff.objects.filter(tariff_type__name="Площадь").first()

    total_billing_price = Decimal("0")

    for flat in flats:
        flat_billing_price = Decimal("0")

        for meter in flat.meters.all():
            tariff_price = meter.tariff.price_per_unit

            for meter_reading in meter.readings.all():
                flat_billing_price += meter_reading.value * tariff_price

        flat_billing_price += flat.area * area_tariff.price_per_unit

        total_billing_price += flat_billing_price

        MonthlyBill.objects.create(
            month=month,
            year=year,
            price=flat_billing_price,
            flat=flat,
            billing_report_id=billing_report_id,
        )

    BillingReport.objects.filter(pk=billing_report_id).update(
        status=BillGenerationStatus.FINISED,
        total=total_billing_price,
    )
