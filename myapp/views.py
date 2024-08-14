from django.http import HttpResponse
from .models import Proyect, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask

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
    #proyectos = list(Proyect.objects.values())  # Convertir el QuerySet a una lista de diccionarios 
    proyects = Proyect.objects.all()
    return render(request, "proyects.html", {
        'proyects' : proyects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse(f"Tarea {task.id}: {task.title}")
    tasks = Task.objects.all()
    return render (request, "tasks.html",{
        "tasks" : tasks 
    })

def create_task(request):
    # mostrar valores por consola
    print(request.GET['title'])
    print(request.GET['description'])
    
    # intanciar objeto para ser guardado en DB
    Task.objects.create(
        title=request.GET['title'],
        description=request.GET['description'],
        proyect_id=2
        # done=False -> configurado por defecto, no se declara.
        )
    
    return render (request, "create_task.html", {
        'form': CreateNewTask()
    })