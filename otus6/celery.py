import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'otus6.settings')

app = Celery('university_app')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
