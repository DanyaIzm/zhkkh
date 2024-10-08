from rest_framework import serializers
from .models import *


class MonthlyBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyBill
        fields = "__all__"


class BillingReportSerializer(serializers.ModelSerializer):
    monthly_bills = MonthlyBillSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = BillingReport
        fields = "__all__"
        read_only_fields = ("status", "total")
