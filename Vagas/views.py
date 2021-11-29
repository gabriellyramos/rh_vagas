
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
import requests

def pesquisa_vagas(request):
    vagas = {}
    todas_vagas = requests.get('http://127.0.0.1:8000/api/vagas/')

    if todas_vagas.status_code in [200, 201]:
        vagas = todas_vagas.json()

    if request.POST:
        titulo = request.POST.get('titulo')
        params = {'titulo': titulo}
        vaga_pesquisada = requests.get('http://127.0.0.1:8000/api/vagas/', params=params)
        vagas = vaga_pesquisada.json()

    context = {
        'vagas': vagas
    }
    return render(request, 'Vagas/pesquisa-vagas.html', context)