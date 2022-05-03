from backend.ponto_certo.apps.cartoes.serializers import CartaoPontoModeloSerializer
from backend.ponto_certo.apps.empresas.serializers import EmpresaSerializer
from backend.ponto_certo.apps.funcionarios.models import Funcionarios
from backend.ponto_certo.apps.registros.serializers import RegistroHorarioSerializer
from rest_framework import serializers


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
