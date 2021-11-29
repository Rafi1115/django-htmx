
from django import forms
from django.forms import ModelForm
from .models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("name",)
        # labels = {
        #     "name": "Add new task:",
        # }