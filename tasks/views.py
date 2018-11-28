from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from tasks.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
