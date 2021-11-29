from django.urls import path
from . import views

urlpatterns = [
    path('vagas/pesquisa_vagas', views.pesquisa_vagas, name='pesquisa_vagas'),
]