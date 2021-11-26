from django.urls import path
from . import views

urlpatterns = [
    path('candidato/cadastro', views.cadastro, name='cadastro'),
    
]