from django.urls import path

from apps.registros import views

app_name = "registros"

urlpatterns = [
    path("", views.RegistroHorarioDetail.as_view(), name="registros"),
]
