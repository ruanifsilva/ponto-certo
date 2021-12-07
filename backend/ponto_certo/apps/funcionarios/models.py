from django.db import models
from backend.ponto_certo.apps.empresas.models import Empresa



class Funcionarios(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField(max_length=11, blank=False)
    funcao = models.CharField(max_length=200)
    data_admissao = models.DateTimeField()

    def __str__(self):
        return self.nome