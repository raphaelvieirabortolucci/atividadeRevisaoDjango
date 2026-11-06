from django.db import models

# Create your models here.

class Categoria(models.Model):
    genero = models.CharField(max_length=20)
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.genero


class Dispositivo(models.Model):
    nome = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=30)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="jogos"
    )
    plataforma = models.ForeignKey(
        Dispositivo,
        on_delete=models.PROTECT,
        related_name="jogos"
    )

    def __str__(self):
        return self.nome
