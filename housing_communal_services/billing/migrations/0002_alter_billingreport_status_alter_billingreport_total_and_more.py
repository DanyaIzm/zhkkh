# Generated by Django 5.1.1 on 2024-10-13 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingreport',
            name='status',
            field=models.CharField(choices=[('PENDING', 'В процессе'), ('FINISHED', 'Завершено'), ('ERROR', 'Ошибка')], default='PENDING', max_length=128, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='billingreport',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='Общая стоимость'),
        ),
        migrations.AlterField(
            model_name='monthlybill',
            name='billing_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_bills', to='billing.billingreport'),
        ),
    ]
