from django.conf.urls import patterns, include, url
from rest_framework import routers
from . import views

todo_router = routers.DefaultRouter()
todo_router.register(r'todos', views.TodoViewSet, base_name='todos')
todo_router.register(r'users', views.UserViewSet, base_name='users')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todo/', views.todo, name='todo'),
    url('^api/', include(todo_router.urls)),
]