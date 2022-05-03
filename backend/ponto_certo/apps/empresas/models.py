from django.db import models


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100)
    cnpj = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.nome_empresa}"
