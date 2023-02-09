from rest_framework import serializers

from .models import Board, Todo


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class BoardListSerializer(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()
