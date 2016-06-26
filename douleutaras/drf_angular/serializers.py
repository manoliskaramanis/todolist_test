from rest_framework import serializers
from drf_angular.models import Todo, User

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'todos')
