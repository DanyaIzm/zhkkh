from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from .tasks import generate_billing_report_task

# Create your views here.


class BillingReportApiView(ListCreateAPIView):
    queryset = BillingReport.objects.all()
    serializer_class = BillingReportSerializer

    def perform_create(self, serializer):
        billing_report = serializer.save()

        generate_billing_report_task.delay(billing_report.id)
