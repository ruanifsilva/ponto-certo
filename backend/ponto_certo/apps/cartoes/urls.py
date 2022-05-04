from django.urls import path

from apps.cartoes import views

app_name = "cartoes"

urlpatterns = [
    path("", views.CartaoPontoModeloDetail.as_view(), name="cartao_modelo"),
]
