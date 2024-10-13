from django.db.models import Prefetch
from django.db.transaction import atomic
from core.models import *
from .exceptions import AreaTariffDoesNotExistError
from .models import *


def generate_billing_report(billing_report_id: int) -> None:
    billing_report = BillingReport.objects.get(id=billing_report_id)

    try:
        _calculate_billing(billing_report)
    except AreaTariffDoesNotExistError:
        billing_report.status = BillGenerationStatus.ERROR
        billing_report.save()

        raise


@atomic
def _calculate_billing(billing_report: BillingReport) -> None:
    flats = Flat.objects.filter(house_id=billing_report.house.id).prefetch_related(
        Prefetch(
            "meters__readings",
            queryset=MeterReading.objects.filter(
                month=billing_report.month, year=billing_report.year
            ),
        ),
        "meters__tariff",
    )

    area_tariff = Tariff.objects.filter(tariff_type__name="Площадь").first()

    if area_tariff is None:
        raise AreaTariffDoesNotExistError(
            'Необходимо добавить тариф с типом "Площадь" перед генерацией отчётов'
        )

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
