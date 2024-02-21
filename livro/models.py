from django.db import models
from autor.models import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publicacao = models.CharField(max_length=4)
    genero = models.CharField(max_length=20)
    
    def __str__(self):
        return self.titulo