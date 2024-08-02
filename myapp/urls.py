from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('proyects/', views.proyects),

    #ruta para vista de tarea
    path('tasks/<int:id>', views.tasks)
]