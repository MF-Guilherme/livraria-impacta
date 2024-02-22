from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro_livros/', views.cadastro, name='cadastro_livros'),
    path('', views.listar, name='livros'),
    path('editar_livro/<int:id_livro>', views.editar_livro, name='editar_livro'),
    path('excluir_livro/<int:id_livro>', views.excluir_livro, name='excluir_livro'),
]
