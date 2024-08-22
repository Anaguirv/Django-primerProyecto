from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('proyects/', views.proyects),

    #ruta para vista de tarea
    #path('tasks/<int:id>', views.tasks)
    path('tasks/', views.tasks),

    #ruta para crear tarea
    path('create_task/', views.create_task),
    
    # ruta para crear proyecto
    path('create_project/', views.create_project)
]