from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tasks.models import Task
from tasks.serializers import TaskSerializer, UserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


#######Task#######
class GetTaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GetTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UpdateTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DeleteTask(mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#######User#######
class GetUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUser(mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#######Endpoints#######
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })

# from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
#
# from tasks.models import CustomUser
# from tasks.serializers import CustomUserSerializer
#
#
# # create user
# @api_view(["POST"])
# def create_user(request):
#     serializer = CustomUserSerializer(request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User created"})
#     else:
#         data = {
#             "error": True,
#             "errors": serializer.errors,
#         }
#         return Response(data)
#
#
# # get user
# @api_view(["GET"])
# def get_user(request, pk):
#     user = CustomUser.objects.get(id=pk)
#     serializer = CustomUserSerializer(user)
#     return Response(serializer.data)
#
#
# # get users list
# @api_view(["GET"])
# def get_users_list(request):
#     users = CustomUser.objects.all()
#     serializer = CustomUserSerializer(users, many=True)
#     return Response(serializer.data)
#
#
# # update user
# @api_view(["GET", "PUT"])
# def update_user(request, pk):
#     user = CustomUser.objects.get(id=pk)
#     if request.method == "PUT":
#         serializer = CustomUserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response({"error": serializer.errors, "error": True})
#     serializer = CustomUserSerializer(user)
#     return Response(serializer.data)
#
#
# # delete user
# def delete_user(request, pk):
#     user = get_object_or_404(CustomUser, id=pk)
#     user.delete()
#     return Response({"message": "Deleted"})
