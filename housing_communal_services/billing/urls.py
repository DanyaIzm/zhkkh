from django.urls import path
from .views import *



urlpatterns = [
    path("billingreports/", BillingReportApiView.as_view()), 
]