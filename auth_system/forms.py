from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from tasks.models import Task

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Enter your email"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter your username"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Create a password"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Repeat your password"
        })

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Enter your username"
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Enter your password"
        })




class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "deadline"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter task title"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe the task..."
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "priority": forms.Select(attrs={
                "class": "form-select"
            }),

            "deadline": forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }),
        }