from django.urls import path
from . import views

app_name = 'to_do'

urlpatterns = [
    path('board-create/', views.BoardCreateApi.as_view()),
    path('board-list/', views.BoardListApi.as_view()),
    path('board-detail_RUD/<int:pk>/', views.BoardDetailRUDApi.as_view()),
    path('To_do-create/', views.TodoCreateApi.as_view()),
    path('To_do-uncompleted/', views.TodoUnCompletedApi.as_view()),
    path('To-do-detail_RUD/<int:pk>/', views.TodoRUDApi.as_view()),
]