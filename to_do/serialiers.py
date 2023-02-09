from rest_framework import serializers

from .models import Board, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'


class BoardListSerializer(serializers.ModelSerializer):
    count_todos = serializers.IntegerField()
    class Meta:
        model = Board
        fields = ['name', 'count_todos']
