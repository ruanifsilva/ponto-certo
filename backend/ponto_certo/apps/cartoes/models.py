from django.db import models

from apps.core.models import TimeStampedModel
from apps.funcionarios.models import Funcionarios
from apps.registros.models import RegistoHorario


class CartaoPontoModelo(TimeStampedModel, models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    cartao_registrado = models.ForeignKey(RegistoHorario, on_delete=models.CASCADE)
    hora_entrada = models.TimeField()
    hora_almoco = models.TimeField()
    hora_volta_almoco = models.TimeField()
    hora_saida = models.TimeField()

    def __str__(self):
        return f"{self.funcionario}"

    class Meta:
        ordering = ["-funcionario"]
        verbose_name = "Mapa"
        verbose_name_plural = "Mapas"
