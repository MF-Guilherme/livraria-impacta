from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Autor
import json
from django.contrib import messages

def cadastro(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        return render(request, 'cadastro.html', {'autores': autores})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        autor = Autor(nome=nome)
        autor.save()
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("/autor/cadastro")

