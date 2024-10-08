from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from core.models import Flat
from core.models import House

# Create your models here.


class BillGenerationStatus(models.TextChoices):
    PENDING = "PENDING", "В процессе"
    FINISED = "FINISHED", "Завершено"


class BillingReport(models.Model):
    status = models.CharField(
        verbose_name="Статус",
        choices=BillGenerationStatus,
        default=BillGenerationStatus.PENDING,
        max_length=128,
    )
    month = models.IntegerField(
        verbose_name="Месяц", validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    year = models.IntegerField(verbose_name="Год")
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=models.CASCADE)
    total = models.DecimalField(
        verbose_name="Общая стоимость",
        decimal_places=2,
        max_digits=16,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"Отчёт {self.id}, статус: {BillGenerationStatus(self.status).label}, сумма: {self.total}"

    class Meta:
        verbose_name = "Отчет по арендной плате дома"
        verbose_name_plural = "Отчеты по арендным плате домов"


class MonthlyBill(models.Model):
    month = models.IntegerField(
        verbose_name="Месяц", validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    year = models.IntegerField(verbose_name="Год")
    price = models.DecimalField(
        verbose_name="Стоимость",
        decimal_places=2,
        max_digits=16,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    flat = models.ForeignKey(Flat, verbose_name="Квартира", on_delete=models.CASCADE)
    billing_report = models.ForeignKey(
        BillingReport, related_name="monthly_bills", on_delete=models.CASCADE
    )
