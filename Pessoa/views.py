from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
import requests

def cadastro(request):
    if request.POST:
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        nascimento = request.POST.get("nascimento")
        telefone = request.POST.get("telefone")
        sexo = request.POST.get("sexo")
        email = request.POST.get("email")

        payload = {'nome': nome, 'sobrenome': sobrenome, 'data_nascimento': nascimento, 'telefone': telefone, 'sexo': sexo, 'email': email}
        
        r = requests.post('http://127.0.0.1:8000/api/pessoas/',data=payload)
        if r.status_code in [200, 201]:
            print("enviar mensagem com o usuario e senha gerados")
    context = {}
    return render(request, 'Pessoa/cadastro.html', context)
