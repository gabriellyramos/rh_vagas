from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
import requests
import string
import random

def geraUsuario():
    qtde = 8
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(qtde))

def cadastro(request):
    if request.POST:
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        nascimento = request.POST.get("nascimento")
        telefone = request.POST.get("telefone")
        sexo = request.POST.get("sexo")
        email = request.POST.get("email")

        payload = {'nome': nome, 'sobrenome': sobrenome, 'data_nascimento': nascimento, 'telefone': telefone, 'sexo': sexo, 'email': email}
        codigo = geraUsuario()
        cad_pessoa = requests.post('http://127.0.0.1:8000/api/pessoas/',data=payload)
        if cad_pessoa.status_code in [200, 201]:
            payload_user = {'username': codigo, 'password': codigo, 'email': email}
            cad_user = requests.post('http://127.0.0.1:8000/api/usuario/',data=payload_user)
            if cad_user.status_code in [200, 201]:
                messages.success(request, 'Cadastro realizado com sucesso. Usuário: {0} e Senha: {0}'.format(codigo))
                return redirect(reverse('login'))
        else:
            messages.error(request, 'Ocorreu um erro, verifique se os dados estão corretos e tente novamente!')
    context = {}
    return render(request, 'Pessoa/cadastro.html', context)
