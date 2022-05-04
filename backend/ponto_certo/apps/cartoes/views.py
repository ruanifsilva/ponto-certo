from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from apps.cartoes.models import CartaoPontoModelo
from apps.cartoes.serializers import CartaoPontoModeloSerializer


class CartaoPontoModeloDetail(generic.DetailView):
    model = CartaoPontoModelo
    Context_object_name = "Cartao_modelo"


class CartaoPontoModeloViewSet(viewsets.ModelViewSet):
    queryset = CartaoPontoModelo.objects.all()
    serializer_class = CartaoPontoModeloSerializer
