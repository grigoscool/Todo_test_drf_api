import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')

app = Celery('test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-5-min': {
        'task': 'send_mail.task.send_beats_spam',
        'schedule': crontab(minute='*/1'),
    },
}
