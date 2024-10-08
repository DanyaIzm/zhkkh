from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from datetime import datetime

from django.forms import ValidationError

# Create your models here.

class House(models.Model):
    """Модель дома"""
    address = models.CharField(verbose_name="Адрес", max_length=256, unique=True)
    area = models.DecimalField(verbose_name="Площадь", decimal_places=2, max_digits=16, validators=[MinValueValidator(Decimal("0.01"))])
    
    def __str__(self) -> str:
        return f"Дом: {self.address}"
    
    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"


class Flat(models.Model):
    """Модель квартиры"""
    # используем CharField, так как могут быть специфичные номера квартир (110/1 или 110A и подобные)
    number = models.CharField(verbose_name="Номер", max_length=128, unique=True)
    house = models.ForeignKey(House, verbose_name="Дом", related_name="flats", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.house}; Квартира {self.number}"
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"


class TariffType(models.Model):
    """Типы тарифов"""
    name = models.CharField(verbose_name="Название типа тарифа", max_length=128, unique=True)

    def __str__(self) -> str:
        return f"Тип тарифа: {self.name}"

    class Meta:
        verbose_name = "Тип тарифа"
        verbose_name_plural = "Типы тарифов"


class Tariff(models.Model):
    """Модель тарифа"""
    price_per_unit = models.DecimalField(verbose_name="Цена за единицу", decimal_places=2, max_digits=16, validators=[MinValueValidator(Decimal("0.01"))])
    tariff_type = models.ForeignKey(TariffType, verbose_name="Тип тарифа", related_name="tariffs", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Тариф: {self.tariff_type.name} за {self.price_per_unit}"

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"


class Meter(models.Model):
    """Модель счётчика в квартире"""
    flat = models.ForeignKey(Flat, verbose_name="Квартира", related_name="meters", on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, verbose_name="Тариф", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Счётчик {self.tariff.tarrif_type}({self.tariff.price_per_unit}) в {self.flat}"

    class Meta:
        verbose_name = "Счётчик"
        verbose_name_plural = "Счётчики"


class MeterReading(models.Model):
    month = models.IntegerField(verbose_name="Месяц", validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.IntegerField(verbose_name="Год")
    meter = models.ForeignKey(Meter, verbose_name="Счётчик", related_name="readings", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.month}.{self.year}; {self.meter}"
    
    def clean(self) -> None:
        current_date = datetime.now()
        
        meter_reading_date = datetime(year=self.year, month=self.month)
        
        if meter_reading_date > current_date:
            raise ValidationError("Дата показания не может быть больше текущего месяца")

    class Meta:
        verbose_name = "Показания счётчика"
        verbose_name_plural = "Показания счётчиков"
