from django.db.models import Prefetch
from core.models import *
from .models import *


def generate_billing_report(billing_report_id: int) -> None:
    billing_report = BillingReport.objects.get(id=billing_report_id)

    flats = Flat.objects.filter(house_id=billing_report.house.id).prefetch_related(
        Prefetch(
            "meters__readings",
            queryset=MeterReading.objects.filter(
                month=billing_report.month, year=billing_report.year
            ),
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
            month=billing_report.month,
            year=billing_report.year,
            price=flat_billing_price,
            flat=flat,
            billing_report_id=billing_report.id,
        )

    billing_report.status = BillGenerationStatus.FINISED
    billing_report.total = total_billing_price
    billing_report.save()
