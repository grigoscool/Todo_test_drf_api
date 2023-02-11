from django.core.mail import EmailMessage


def send(user_email, text):
    msg = EmailMessage('reminder',
                       [text], to=[user_email])
    msg.send()
