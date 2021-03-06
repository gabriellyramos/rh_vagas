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
from .apis import PessoasView, VagasView, UsuarioView, CustomAuthToken, UploadCurriculum, CurriculumPDFView
from . import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('', views.logout, name="logout"),
    path('api/token/', CustomAuthToken.as_view(), name='token'),
    path('api/pessoas/', PessoasView.as_view(), name='pessoas'),
    path('api/usuario/', UsuarioView.as_view(), name='usuarios'),
    path('api/vagas/', VagasView.as_view(), name='vagas'),
    path('api/curriculum/', UploadCurriculum.as_view(), name='curriculums'),
    path('api/open_curriculum/<int:pk>', CurriculumPDFView.as_view(), name='open_curriculum'),
    path('Pessoa', include(('Pessoa.urls', 'Pessoa'), namespace='Pessoa')),
    path('Vagas', include(('Vagas.urls', 'Pessoa'), namespace='Vagas')),
]
