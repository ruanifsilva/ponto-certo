from django.db import models
from backend.ponto_certo.apps.funcionarios.models import Funcionarios


class RegistoHorario(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    mes_de_trabalho = models.CharField(max_length=10)
    hora_entrada = models.DateTimeField()
    hora_saida_almoco = models.DateTimeField()
    hora_volta_almoco = models.DateTimeField()
    hora_saida = models.DateTimeField()

    def __str__(self):
        return f'Cartão referente ao funcionário {self.funcionario}'