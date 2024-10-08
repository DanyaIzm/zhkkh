import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'housing_communal_services.settings')

app = Celery('housing_communal_services')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
