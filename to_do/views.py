from django.db.models import Count
from rest_framework import generics, permissions

from .models import Board, Todo
from .permissions import IsOwnerOrAdmin
from .serialiers import BoardSerializer, BoardListSerializer, TodoSerializer


class BoardCreateApi(generics.CreateAPIView):
    """
    Creation a new board
    * permission only for auth user
    """
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class BoardListApi(generics.ListAPIView):
    """
    Board list with names and count_todos only
    * permission only for auth user
    """
    serializer_class = BoardListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return Board.objects.all().annotate(count_todos=Count('todos'))


class BoardDetailRUDApi(generics.RetrieveUpdateDestroyAPIView):
    """
    CUD for board and detail view
    * permission only for owner or staff
    """
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin, ]
    queryset = Board.objects.all()


class TodoCreateApi(generics.CreateAPIView):
    """
    Create new To_do
    * permission only for auth user
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class TodoUnCompletedApi(generics.ListAPIView):
    """
    Show uncomleted to_do
    * permission only for auth user
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return Todo.objects.filter(done=False)


class TodoRUDApi(generics.RetrieveUpdateDestroyAPIView):
    """
    RUD To_do and detail view
    * permission only for auth user
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin, ]
    queryset = Todo.objects.all()
