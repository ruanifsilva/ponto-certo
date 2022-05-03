from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from apps.empresas.models import Empresa
from apps.empresas.serializers import EmpresaSerializer


class EmpresaList(generic.ListView):
    model = Empresa
    context_object_name = "Lista_empresas"


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by("-nome_empresa")
    serializer_class = EmpresaSerializer
