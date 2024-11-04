from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
