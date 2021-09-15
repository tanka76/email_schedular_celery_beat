from __future__ import absolute_import,unicode_literals
from datetime import timezone
import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerydjango.settings')

app = Celery('celerydjango')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#app.conf.enable_utc=False
#app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-60sec': {
        'task': 'app1.tasks.send_mail_with_celery',
        'schedule':60
        #'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year = 6),
        #'args': (2,)
    }
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
