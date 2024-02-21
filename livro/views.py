from django.shortcuts import render, redirect
from .models import Livro 
from autor.models import Autor
from django.contrib import messages
from django.http import HttpResponse

def cadastro(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        return render(request, 'cadastro_livros.html', {'autores': autores})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor_id = int(request.POST.get('autor'))  # Convertendo para inteiro
        publicacao = request.POST.get('publicacao')
        genero = request.POST.get('genero')
        livro = Livro(titulo=titulo, autor_id=autor_id, publicacao=publicacao, genero=genero)
        livro.save()
        messages.success(request, "Livro cadastrado com sucesso!")
        return redirect("/livros/")

def listar(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})
