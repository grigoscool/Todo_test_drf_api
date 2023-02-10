from django.urls import path

from . import views


app_name = 'send'

urlpatterns = [
    path('', views.SendMail.as_view(), name='mail'),
]