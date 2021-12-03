from django.db import models


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100)
    cnpj = models.IntegerField(max_length=14, blank=False)

    def __str__(self):
        return self.nome_empresa