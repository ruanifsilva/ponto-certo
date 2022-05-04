from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from apps.funcionarios.models import Funcionarios
from apps.funcionarios.serializers import FuncionariosSerializer


class FuncionariosDetail(generic.DetailView):
    model = Funcionarios
    context_object_name = "Funcionarios"


class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all().order_by("-nome")
    serializer_class = FuncionariosSerializer
