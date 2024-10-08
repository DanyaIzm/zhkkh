from celery import shared_task
from .services import generate_billing_report
from .models import BillingReport


@shared_task
def generate_billing_report_task(billing_report: BillingReport):
    generate_billing_report(billing_report)
