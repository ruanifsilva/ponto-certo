from rest_framework import serializers

from apps.cartoes.serializers import CartaoPontoModeloSerializer
from apps.empresas.serializers import EmpresaSerializer
from apps.funcionarios.models import Funcionarios
from apps.registros.serializers import RegistroHorarioSerializer


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        empresa = EmpresaSerializer(many=False, read_only=False, required=True)

        cartao_mapa = CartaoPontoModeloSerializer(
            many=True, read_only=False, required=True
        )
        registro_diario = RegistroHorarioSerializer(
            many=True, read_only=False, required=True
        )

        model = Funcionarios
        fields = ["id", "nome", "cpf", "funcao", "data_admissao"]
