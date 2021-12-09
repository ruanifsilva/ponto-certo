from backend.ponto_certo.apps.core.models import TimeStampedModel
from backend.ponto_certo.apps.empresas.models import Empresa
from django.db import models


class Funcionarios(models.Model, TimeStampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField(max_length=11, blank=False)
    funcao = models.CharField(max_length=200)
    data_admissao = models.DateTimeField()

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        ordering = "-nome"
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
