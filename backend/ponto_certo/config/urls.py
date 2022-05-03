"""ponto_certo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.empresas.views import EmpresaViewSet

router = routers.DefaultRouter()
router.register(r"empresas", EmpresaViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path("cartoes/", include("apps.cartoes.urls", namespace="cartoes")),
    path("empresas/", include("apps.empresas.urls", namespace="empresas")),
    path("funcionarios/", include("apps.funcionarios.urls", namespace="funcionarios")),
    path("registros/", include("apps.registros.urls", namespace="registros")),
    # urlpatterns da API
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
