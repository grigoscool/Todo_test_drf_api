from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Board, Todo
from .serialiers import BoardSerializer, BoardListSerializer, TodoSerializer
from django.db.models import Count
from .permissions import IsOwnerOrAdmin

class BoardCreateApi(generics.CreateAPIView):
    """ Creation a new board """
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class BoardListApi(generics.ListAPIView):
    """ Board list with names and count_todos only """
    serializer_class = BoardListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return Board.objects.all().annotate(count_todos=Count('todos'))


class BoardDetailRUDApi(generics.RetrieveUpdateDestroyAPIView):
    """ CUD for board and detail view """
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin, ]
    queryset = Board.objects.all()


class TodoCreateApi(generics.CreateAPIView):
    """ Create new To_do """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class TodoUnCompletedApi(generics.ListAPIView):
    """ Show uncomleted to_do """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return Todo.objects.filter(done=False)


class TodoRUDApi(generics.RetrieveUpdateDestroyAPIView):
    """ RUD To_do and detail view """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin, ]
    queryset = Todo.objects.all()

