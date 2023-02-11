from django.contrib import admin

from .models import Todo, Board

admin.site.register(Board)
admin.site.register(Todo)
