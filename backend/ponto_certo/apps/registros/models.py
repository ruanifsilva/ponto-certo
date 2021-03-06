from django.db import models

from apps.core.models import TimeStampedModel
from apps.funcionarios.models import Funcionarios


class RegistoHorario(TimeStampedModel, models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    mes_de_trabalho = models.DateTimeField()
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()

    def __str__(self):
        return f"Cartão referente ao funcionário {self.funcionario}"

    class Meta:
        ordering = ["-funcionario"]
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
