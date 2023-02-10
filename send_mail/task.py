from test.celery import app
from .servises import send



@app.task
def send_spam(user_email):
    send(user_email)
