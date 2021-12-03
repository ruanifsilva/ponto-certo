from django.db import models
from backend.ponto_certo.apps.empresas.models import Empresa
from backend.ponto_certo.apps.cartoes.models import CartaoPontoModelo


class Funcionarios(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cartao_ponto_modelo = models.ForeignKey(CartaoPontoModelo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField(max_length=11, blank=False)
    funcao = models.CharField(max_length=200)
    data_admissao = models.DateTimeField()

    def __str__(self):
        return self.nome