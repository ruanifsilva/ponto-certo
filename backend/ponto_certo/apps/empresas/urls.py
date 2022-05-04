from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.empresas import views

app_name = "empresas"

urlpatterns = [
    path("", views.EmpresaList.as_view(), name="lista_de_empresas"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
