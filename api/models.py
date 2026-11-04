from django.db import models

# Create your models here.


class Categorias(models.Model):
    genero = models.CharField(max_length=20)
    plataforma = models.CharField(max_length=100)
    descricao = models.TextField(max_length= 255)
    ativo = models.BooleanField(default= True)

    def __str__(self):
        return self.genero

class jogo(models.Model):
    nome = models.CharField(max_length= 255)
    