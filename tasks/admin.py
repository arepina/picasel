from django.contrib import admin

from tasks.models import User, Task

admin.site.register(User)
admin.site.register(Task)

