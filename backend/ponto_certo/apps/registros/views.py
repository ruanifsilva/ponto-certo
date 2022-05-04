from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from apps.registros.models import RegistoHorario
from apps.registros.serializers import RegistroHorarioSerializer


class RegistroHorarioDetail(generic.DetailView):
    model = RegistoHorario
    Context_object_name = "Cartao_modelo"


class RegistroHorarioDetailViewSet(viewsets.ModelViewSet):
    queryset = RegistoHorario.objects.all()
    serializer_class = RegistroHorarioSerializer
