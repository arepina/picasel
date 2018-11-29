from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tasks.models import Task, CustomUser
from tasks.serializers import TaskSerializer, CustomUserSerializer


#######Task#######

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


#######CustomUser#######
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



#######Endpoints#######
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })


# create user
@api_view(["POST"])
def create_user(request):
    serializer = CustomUserSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"})
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data)


# get user
@api_view(["GET"])
def get_user(request, pk):
    user = CustomUser.objects.get(id=pk)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


# get users list
@api_view(["GET"])
def get_users_list(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


# update user
@api_view(["GET", "PUT"])
def update_user(request, pk):
    user = CustomUser.objects.get(id=pk)
    if request.method == "PUT":
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True})
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


# delete user
def delete_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    user.delete()
    return Response({"message": "Deleted"})


# create task
@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Task created"})
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data)


# get task
@api_view(["GET"])
def get_task(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


# get tasks list
@api_view(["GET"])
def get_tasks_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# update task
@api_view(["GET", "PUT"])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True})
    serializer = TaskSerializer(task)
    return Response(serializer.data)


# delete task
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response({"message": "Deleted"})
