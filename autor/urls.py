from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar_autor/<int:id_autor>', views.editar_autor, name='editar_autor')
]
