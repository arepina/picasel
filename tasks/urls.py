from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from tasks import views

urlpatterns = [
    path('tasks/', views.GetTaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.GetTask.as_view()),
    path('users/', views.GetUserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.GetUser.as_view()),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)