from rest_framework import serializers

from tasks.models import Task, CustomUser


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ("name", "definition", "owner", "checker")


class CustomUserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Task.objects.all())

    class Meta:
        model = CustomUser
        fields = ("id", "username", "task", "position", "city")
