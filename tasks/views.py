from auth_system.forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")
    login_url = "login"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task_list")