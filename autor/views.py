from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Autor
import json
from django.contrib import messages

def cadastro(request):
    if request.method == 'GET':
        autores = Autor.objects.all().order_by('nome')
        return render(request, 'cadastro.html', {'autores': autores})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        autor = Autor(nome=nome)
        autor.save()
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("/autores/cadastro")

def editar_autor(request, id_autor):
    if request.method == 'GET':
        autor = Autor.objects.filter(id=id_autor)[0]
        return render(request, 'editar_autor.html', {'autor': autor})
    elif request.method == 'POST':
        autor = Autor.objects.filter(id=id_autor)[0]
        nome = request.POST.get('nome')
        autor.nome = nome
        autor.save()
        messages.success(request, "Cadastro atualizado com sucesso!")
        return redirect("/autores/cadastro")

def excluir_autor(request, id_autor):
    if request.method == 'GET':
        autor = Autor.objects.filter(id=id_autor)[0]
        return render(request, 'excluir_autor.html', {'autor': autor})
    elif request.method == 'POST':
        autor = Autor.objects.filter(id=id_autor)[0]
        autor.delete()
        messages.success(request, "Cadastro excluído com sucesso!")
        return redirect("/autores/cadastro")
