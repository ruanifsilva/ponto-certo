from rest_framework import serializers

from backend.ponto_certo.apps.empresas.models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["id", "nome_empresa", "cnpj"]
