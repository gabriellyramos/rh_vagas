from django.db import models

# Create your models here.
class Pessoa(models.Model):
    
    CHOICES_SEXO = (       
        (0, "Não binário"),             
        (1, "Feminino"),
        (2, "Masculino")
    )

    nome = models.CharField(max_length=30, null=True, blank=True)
    sobrenome = models.CharField(max_length=30, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    sexo = models.IntegerField(choices=CHOICES_SEXO, default=0)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
