from django.urls import path

from apps.funcionarios import views

app_name = "funcionarios"

urlpatterns = [
    path("", views.FuncionariosDetail.as_view(), name="detalhes_funcionarios")
]
