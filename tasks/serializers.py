from rest_framework import serializers

from tasks.models import Task
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ("name", "definition", "owner")


class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "task")



