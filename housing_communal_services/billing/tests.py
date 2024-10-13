from django.test import TestCase

from billing.services import generate_billing_report
from .models import *
from .exceptions import AreaTariffDoesNotExistError
from core.models import *
from decimal import Decimal


class ReportGenerationTests(TestCase):
    def test_total_correct(self):
        tariff_type = TariffType.objects.create(name="Вода")

        tariff1 = Tariff.objects.create(
            price_per_unit=Decimal("20"), tariff_type=tariff_type
        )
        tariff2 = Tariff.objects.create(
            price_per_unit=Decimal("40"), tariff_type=tariff_type
        )

        area_tariff_type = TariffType.objects.create(name="Площадь")

        tariff1_area = Tariff.objects.create(
            price_per_unit=Decimal("10"), tariff_type=area_tariff_type
        )

        house = House.objects.create(address="123")
        flat1 = Flat.objects.create(number="1231", area=50, house=house)
        flat2 = Flat.objects.create(number="1232", area=60, house=house)

        meter11 = Meter.objects.create(flat=flat1, tariff=tariff1)
        meter12 = Meter.objects.create(flat=flat1, tariff=tariff2)
        meter21 = Meter.objects.create(flat=flat2, tariff=tariff1)
        meter22 = Meter.objects.create(flat=flat2, tariff=tariff2)

        meter_reading11 = MeterReading.objects.create(
            month=1, year=2000, meter=meter11, value=Decimal("1")
        )
        meter_reading12 = MeterReading.objects.create(
            month=1, year=2000, meter=meter12, value=Decimal("1")
        )
        meter_reading21 = MeterReading.objects.create(
            month=1, year=2000, meter=meter21, value=Decimal("2")
        )
        meter_reading22 = MeterReading.objects.create(
            month=1, year=2000, meter=meter22, value=Decimal("2")
        )

        meter_reading_incorrect1 = MeterReading.objects.create(
            month=2, year=2000, meter=meter22, value=Decimal("777")
        )
        meter_reading_incorrect2 = MeterReading.objects.create(
            month=1, year=2001, meter=meter22, value=Decimal("777")
        )

        billing_report = BillingReport.objects.create(
            month=1, year=2000, house_id=house.id
        )

        generate_billing_report(billing_report_id=billing_report.id)

        billing_report.refresh_from_db()

        # ((50 * 10) + 1 * 20 + 1 * 40) +  ((60 * 10) + 2 * 20 + 2 * 40) = 1280
        self.assertEqual(billing_report.status, BillGenerationStatus.FINISED)
        self.assertEqual(billing_report.total, Decimal("1280"))

    def test_area_tarrif_does_not_exist(self):
        house = House.objects.create(address="123")
        billing_report = BillingReport.objects.create(
            month=1, year=2000, house_id=house.id
        )

        with self.assertRaises(AreaTariffDoesNotExistError):
            generate_billing_report(billing_report_id=billing_report.id)
