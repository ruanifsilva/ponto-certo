from django.urls import path

from apps.empresas import views
from apps.empresas.views import EmpresaList

app_name = "empresas"

urlpatterns = [
    path("", views.EmpresaList.as_view(), name="empresalist"),
]
