from django.http import HttpResponse, JsonResponse
from .models import Proyect, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = "Django Course"
    return render(request, 'index.html', {
        "titulo" : title
    })

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return render(request,"about.html")

def proyects(request):
    proyectos = list(Proyect.objects.values())  # Convertir el QuerySet a una lista de diccionarios 
    return JsonResponse(proyectos, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"Tarea {task.id}: {task.title}")