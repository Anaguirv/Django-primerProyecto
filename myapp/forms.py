from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo tarea", max_length=200)
    description = forms.CharField(label="Descripción de la tarea" ,widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre proyecto", max_length=200)