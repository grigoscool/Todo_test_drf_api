from django.core.mail import send_mail
from test.celery import app
from .servises import send
from .models import Reminder


@app.task
def remind_mail(user_email, text):
    send(user_email, text)


# @app.task
# def send_beat_remind():
#     for m in Reminder.objects.all():
#         send_mail(
#             'remind',
#             [m.text],
#             'grigoscool@mail.ru',
#             [m.email],
#             fail_silently=False,
#         )
