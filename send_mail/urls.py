from django.urls import path

from . import views

app_name = 'send'

urlpatterns = [
    # path('', views.SendMail.as_view(), name='mail'),

    path('remind-create/', views.ReminderCreateAPI.as_view()),
    path('remind-list/', views.ReminderListApi.as_view()),
    path('remind-RUD/<int:pk>/', views.ReminderRUD.as_view()),
]
