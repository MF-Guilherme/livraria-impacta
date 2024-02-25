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
    autores = Autor.objects.all()
    return render(request, 'livros.html', {'livros': livros, 'autores': autores})


def editar_livro(request, id_livro):
    if request.method == 'GET':
        livro = Livro.objects.filter(id=id_livro)[0]
        autores = Autor.objects.all()
        return render(request, 'editar_livro.html', {'livro': livro, 'autores': autores})
    elif request.method == 'POST':
        livro = Livro.objects.filter(id=id_livro)[0]
        livro.titulo = request.POST.get('titulo')
        livro.autor_id = int(request.POST.get('autor'))
        livro.publicacao = request.POST.get('publicacao')
        livro.genero = request.POST.get('genero')
        livro.save()
        messages.success(request, "Alterações salvas com sucesso!")
        return redirect('/livros/')


def excluir_livro(request, id_livro):
    if request.method == 'GET':
        livro = Livro.objects.filter(id=id_livro)[0]
        return render(request, 'excluir_livro.html', {'livro': livro})
    elif request.method == 'POST':
        livro = Livro.objects.get(id=id_livro)
        livro.delete()
        messages.success(request, "Cadastro excluído com sucesso!")
        return redirect('/livros/')


def livros_por_autor(request, id_autor):
    livros = Livro.objects.filter(autor=id_autor)
    autores = Autor.objects.all()
    return render(request, 'livros_por_autor.html', {'livros': livros, 'autores': autores})