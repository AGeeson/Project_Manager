from django import forms
from .models import Project, Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        progress = forms.ChoiceField(
            choices=Task.PROGRESS, widget=forms.Select(attrs={"onChange": 'submit();'}))
        fields = ['name', 'progress', 'essential']
        labels = {'name': '', 'essential': 'essential'}


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'notes']


class EditForm(forms.ModelForm):

    class Meta:
        model = Task
        progress = forms.ChoiceField(
            choices=Task.PROGRESS, widget=forms.Select(attrs={"onChange": 'submit();', "name": 'c{{task.id}}'}))
        fields = ['name', 'progress']
        labels = {'name': ''}


class EEditForm(forms.ModelForm):

    class Meta:
        model = Task
        progress = forms.ChoiceField(
            choices=Task.PROGRESS, widget=forms.Select(attrs={"onChange": 'submit();'}))
        fields = ['name', 'progress', 'id']
        labels = {'name': ''}


class TaskChanegForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['progress']
