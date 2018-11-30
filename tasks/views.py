from django.core import serializers
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tasks.models import Task, CustomUser
from tasks.serializers import TaskSerializer, CustomUserSerializer


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class DetailTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CustomUserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        position = self.request.query_params.get('position', None)
        if position is not None:
            queryset = queryset.filter(position=position)
        return queryset


class DetailCustomUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view(['GET'])
def user_tasks(request, user):
    queryset = Task.objects.filter(owner=user)
    data = serializers.serialize('json', queryset)
    return Response(data, content_type="None")


@api_view(['GET'])
def task_users(request, task):
    queryset = CustomUser.objects.filter(task=task)
    data = serializers.serialize('json', queryset)
    return Response(data, content_type="None")


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })
