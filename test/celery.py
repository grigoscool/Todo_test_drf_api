import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')

app = Celery('test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'remind-mail': {
#         'task': 'send_mail.task.send_beat_remind',
#         'schedule': crontab(minute='*/1'),
#     },
# }
