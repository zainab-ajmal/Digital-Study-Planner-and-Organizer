from django import forms
from .models import stickyNote, Notebook
from tinymce.widgets import TinyMCE

from .models import Task

class stickyNotesForm(forms.ModelForm):
    class Meta:
        model=stickyNote
        fields =('title','text')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-3'}),
            'text':  forms.Textarea(attrs={'class':'form-control my-3'}),
            
        }
        labels={
            'text':'Write your thoughts'
        }

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notebook
        fields =('title','text')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-3'}),
            'text': TinyMCE(attrs={'class': 'form-control my-3', 'cols': 80, 'rows': 30}), 
            
        }
        labels={
            'text':'Write your thoughts'
        }



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'task-input',
                'placeholder': 'Add a new task'
            }),
        }