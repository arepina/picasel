from django.conf.urls import url
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from tasks import views

urlpatterns = [
    url(r'^tasks/$', views.TaskView.as_view(), name='task-list'),
    url(r'^tasks/(?P<pk>\d+)/$', views.DetailTaskView.as_view()),
    url(r'^users/$', views.CustomUserView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', views.DetailCustomUserView.as_view()),
    url(r'^user_tasks/(?P<user>\d+)/$', views.user_tasks),
    url(r'^task_users/(?P<task>\d+)/$', views.task_users),
    url(r'^check_assign/(?P<task_id>\d+)/(?P<username>\w+)/$', views.check_assign),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)