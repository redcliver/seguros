from django.db import models
from django.utils import timezone

# Create your models here.
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    data_nasc = models.DateTimeField(default=timezone.now)
    venc_habilitacao = models.DateTimeField(default=timezone.now)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome