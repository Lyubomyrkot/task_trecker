from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='create_tasks'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
]