from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('proyects/', views.proyects),

    #ruta oara vista de tarea
    path('tasks/<int:id>', views.tasks)
]