from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from tasks import views

urlpatterns = [
    path('tasks/', views.TaskView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.DetailTaskView.as_view()),
    path('users/', views.CustomUserView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.DetailCustomUserView.as_view()),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)