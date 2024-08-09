from django import forms

class CreateNewTask():
    title = forms.CharField(label="Titulo tarea", max_length=200)
    description = forms.Textarea(label="aaa", required=False)