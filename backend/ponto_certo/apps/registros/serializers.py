from backend.ponto_certo.apps.registros.models import RegistoHorario
from rest_framework import serializers


class RegistroHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistoHorario
        fields = [
            "id",
            "funcionario",
            "mes_de_trabalhado",
            "hora_entrada",
            "hora_saida",
        ]
