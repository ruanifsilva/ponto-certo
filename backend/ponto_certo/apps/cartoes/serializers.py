from rest_framework import serializers

from apps.cartoes.models import CartaoPontoModelo


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
