from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro_livros/', views.cadastro, name='cadastro_livros'),
    path('', views.listar, name='livros')
]
