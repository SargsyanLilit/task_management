from django import forms
from helpers.choices import STATUS_CHOICES
from django.core.exceptions import ValidationError
from task.models import Task
from django.views.generic.edit import UpdateView


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    def clean_name(self):
        name = self.cleaned_data['name']
        task = Task.objects.filter(name=name)
        if task:
            raise ValidationError("Task with this name already exists")
        return name


class TaskUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status']
