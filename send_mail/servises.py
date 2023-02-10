from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect


def send(user_email):
    msg = EmailMessage('Request Callback',
                       'Here is the message.', to=[user_email])
    msg.send()
    return HttpResponseRedirect('/')
