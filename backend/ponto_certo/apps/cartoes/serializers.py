from backend.ponto_certo.apps.cartoes.models import CartaoPontoModelo
from rest_framework import serializers


class CartaoPontoModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaoPontoModelo
        fields = [
            "id",
            "funcionario",
            "cartao_registrado",
            "hora_entrada",
            "hora_almoco",
            "hora_volta_almoco",
            "hora_saida",
        ]
