from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.empresas.models import Empresa
from apps.empresas.serializers import EmpresaSerializer


class EmpresaList(APIView):
    def get(self, request, format=None):
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by("-nome_empresa")
    serializer_class = EmpresaSerializer
