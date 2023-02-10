from django.core.mail import send_mail
from test.celery import app
from .servises import send
from .models import Reminder


# @app.task
# def send_spam(user_email):
#     send(user_email)
#
#
# @app.task
# def send_beats_spam():
#     for m in Mail.objects.all():
#         send_mail(
#             'рассылка',
#             'письмо каждые 5 мин',
#             'grigoscool@mail.ru',
#             [m.email],
#             fail_silently=False,
#         )
