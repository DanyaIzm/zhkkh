# Generated by Django 5.1.1 on 2024-10-08 19:55

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Цена за единицу')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='TariffType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название типа тарифа')),
            ],
            options={
                'verbose_name': 'Тип тарифа',
                'verbose_name_plural': 'Типы тарифов',
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128, verbose_name='Номер')),
                ('area', models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Площадь')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='core.house', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
                'unique_together': {('house', 'number')},
            },
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meters', to='core.flat', verbose_name='Квартира')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tariff', verbose_name='Тариф')),
            ],
            options={
                'verbose_name': 'Счётчик',
                'verbose_name_plural': 'Счётчики',
            },
        ),
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Месяц')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('value', models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Показания')),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='core.meter', verbose_name='Счётчик')),
            ],
            options={
                'verbose_name': 'Показания счётчика',
                'verbose_name_plural': 'Показания счётчиков',
            },
        ),
        migrations.AddField(
            model_name='tariff',
            name='tariff_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tariffs', to='core.tarifftype', verbose_name='Тип тарифа'),
        ),
    ]
