from django.db import models

class Vagas(models.Model):
    titulo = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    requisitos = models.CharField(max_length=100, null=True, blank=True)
