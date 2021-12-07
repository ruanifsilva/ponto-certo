from django.db import models
from backend.ponto_certo.apps.registros.models import RegistoHorario
from backend.ponto_certo.apps.funcionarios.models import Funcionarios


class CartaoPontoModelo(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    cartao_registrado = models.ForeignKey(RegistoHorario, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField()
    hora_saida_almoco = models.DateTimeField()
    hora_volta_almoco = models.DateTimeField()
    hora_saida = models.DateTimeField()

