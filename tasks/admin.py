from django.contrib import admin

from tasks.models import Task, CustomUser

admin.site.register(Task)
admin.site.register(CustomUser)

