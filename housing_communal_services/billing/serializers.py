from rest_framework import serializers
from .models import *


class MonthlyBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyBill
        fields = "__all__"


class BillingReportSerializer(serializers.ModelSerializer):
    flat_bill = MonthlyBillSerializer(many=True, read_only=True)
    
    class Meta:
        model = BillingReport
        fields = "__all__"
        read_only_fields = ("status", "total")
