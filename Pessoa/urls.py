from django.urls import path
from . import views

urlpatterns = [
    path('candidato/cadastro', views.cadastro, name='cadastro'),
    path('candidato/area_restrita', views.area_restrita, name='area_restrita'),
    
]