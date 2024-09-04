from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'due_date']
        # widgets = {
        #     'complete': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
        #     'due_date': forms.DateTimeField(attrs={'class': 'form-control', 'type': 'date'})
        # }

        title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter task description'})
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )