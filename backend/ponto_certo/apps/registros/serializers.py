from rest_framework import serializers

from apps.registros.models import RegistoHorario


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
