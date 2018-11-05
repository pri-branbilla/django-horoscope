from django.db import models

# Create your models here.
class Signos(models.Model):
    nome = models.CharField(max_length=200)
    data = models.CharField(max_length=200, default=" ")
    descricao = models.TextField()
    img = models.CharField(max_length=1000)
    nomelink = models.CharField(max_length=200)
    def __str__(self):
        return self.nome
