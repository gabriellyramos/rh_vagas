"""rh_vagas URL Configuration

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
from django.urls import path
from .apis import PessoasView, VagasView, VagasDisponiveisView
from . import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('api/pessoas/', PessoasView.as_view(), name='pessoas'),
    path('api/vagas/', VagasView.as_view(), name='vagas'),
    path('api/vagas_disponiveis/', VagasDisponiveisView.as_view(), name='vagas_disponiveis'),
    path('Pessoa', include(('Pessoa.urls', 'Pessoa'), namespace='Pessoa')),
]
