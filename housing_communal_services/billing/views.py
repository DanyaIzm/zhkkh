from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from .tasks import debug_task

# Create your views here.

class BillingReportApiView(ListCreateAPIView):
    queryset = BillingReport.objects.all()
    serializer_class = BillingReportSerializer
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
