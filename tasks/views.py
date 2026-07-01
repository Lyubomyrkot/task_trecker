from .models import Task
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.utils import timezone


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class DashboardView(ListView):
    model = Task
    template_name = 'dashboard.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = context["tasks"]

        context["total_tasks"] = tasks.count()

        context["in_progress"] = tasks.filter(status="in_progress").count()

        context["completed"] = tasks.filter(status="completed").count()

        context["overdue"] = tasks.filter(
            deadline__lt=timezone.now()
        ).exclude(status="completed").count()

        context["high_tasks"] = tasks.filter(priority="high").count()
        context["medium_tasks"] = tasks.filter(priority="medium").count()
        context["low_tasks"] = tasks.filter(priority="low").count()

        return context

class TaskCreateView(ListView):
    model = Task
    template_name = 'create_tasks.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"

class ProfileView(ListView):
    model = Task
    template_name = 'profile.html'
    context_object_name = 'tasks'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["profile.html"]
        return ["guest_profile.html"]