from django.shortcuts import render
from rest_framework import viewsets
from drf_angular.models import Todo, User
from serializers import TodoSerializer, UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        if(self.request.query_params.get('user_id', None) == None):
            #case of update and delete
            return Todo.objects.all()
        else:
            #case of getting todos of a user
            return Todo.objects.filter(user=User.objects.filter(id=self.request.query_params.get('user_id', None)))

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if(self.request.query_params.get('password', None) == None):
            #case of checking existance of username
            return User.objects.filter(username=self.request.query_params.get('username', None))
        else:
            #case of login
            return User.objects.filter(username=self.request.query_params.get('username', None), password=self.request.query_params.get('password', None))


def index(request):
    return render(request, 'drf_angular/index.html')

def todo(request):
    return render(request, 'drf_angular/todo.html')

