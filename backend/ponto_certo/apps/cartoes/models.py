from backend.ponto_certo.apps.core.models import TimeStampedModel
from backend.ponto_certo.apps.funcionarios.models import Funcionarios
from backend.ponto_certo.apps.registros.models import RegistoHorario
from django.db import models


class CartaoPontoModelo(models.Model, TimeStampedModel):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    cartao_registrado = models.ForeignKey(RegistoHorario, on_delete=models.CASCADE)
    hora_entrada = models.TimeField()
    hora_almoco = models.TimeField()
    hora_volta_almoco = models.TimeField()
    hora_saida = models.TimeField()

    def __str__(self):
        return f'{self.funcionario}'

    class Meta:
        ordering = '-funcionario'
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'
