from django.contrib.auth.models import AbstractUser
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    definition = models.CharField(max_length=100, null=False)
    owner = models.ForeignKey('tasks.CustomUser', related_name='task', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    position = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
