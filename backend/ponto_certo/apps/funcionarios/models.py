from django.db import models

from apps.core.models import TimeStampedModel
from apps.empresas.models import Empresa


class Funcionarios(TimeStampedModel, models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField(blank=False)
    funcao = models.CharField(max_length=200)
    data_admissao = models.DateTimeField()

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        ordering = ["-nome"]
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
