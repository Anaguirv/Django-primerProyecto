from django.http import HttpResponse
from .models import Proyect, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

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
    return render(request, "projects/proyects.html", {
        'proyects' : proyects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse(f"Tarea {task.id}: {task.title}")
    tasks = Task.objects.all()
    return render (request, "tasks/tasks.html",{
        "tasks" : tasks 
    })

def create_task(request):
    if request.method == 'GET':
        return render (request, "tasks/create_task.html", {
            'form': CreateNewTask()
        })
    else:
        # instanciar objeto de "Task" para ser guardado en DB
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            proyect_id=2
            # done=False -> configurado por defecto, no se declara.
            )
        return redirect('tasks')
    
def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            'form': CreateNewProject()
        })
    else:
        # instanciar el objeto de "Proyect" para ser guardado en DB
        Proyect.objects.create(
            name=request.POST['name']
        )
        return redirect('projects')