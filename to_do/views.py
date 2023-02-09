from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Board, Todo
from .serialiers import BoardSerializer, BoardListSerializer, TodoSerializer
from django.db.models import Count


class BoardCreateApi(generics.CreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class BoardListApi(generics.ListAPIView):
    serializer_class = BoardListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return Board.objects.all().annotate(count_todos=Count('todos'))


class BoardDetailApi(generics.RetrieveAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Board.objects.all()
