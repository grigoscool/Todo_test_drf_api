from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Board(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
