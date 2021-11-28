from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
import requests
import string
import random
from django.contrib.auth.decorators import login_required
from django import forms
from django.core.validators import FileExtensionValidator
from Vagas.models import Vagas
from Curriculum.models import Curriculum

class UploadForm(forms.Form):
    arquivo = forms.FileField(required=False,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


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

        codigo = geraUsuario()
        payload_user = {'username': codigo, 'password': codigo, 'email': email, 'is_active': True}
        cad_user = requests.post('http://127.0.0.1:8000/api/usuario/',data=payload_user)
        if cad_user.status_code in [200, 201]:
            retorno = cad_user.json()
            
            payload = {
                'nome': nome, 
                'sobrenome': sobrenome, 
                'data_nascimento': nascimento, 
                'telefone': telefone, 
                'sexo': sexo, 
                'email': email,
                'usuario': retorno.get("id")}
            
            cad_pessoa = requests.post('http://127.0.0.1:8000/api/pessoas/',data=payload)

            if cad_pessoa.status_code in [200, 201]:
                messages.success(request, 'Cadastro realizado com sucesso. Usuário: {0} e Senha: {0}'.format(codigo))
                return redirect(reverse('Pessoa:cadastro'))
                
            else:
                messages.error(request, 'Ocorreu um erro, verifique se os dados estão corretos e tente novamente!')
        else:
                messages.error(request, 'Ocorreu um erro, verifique se os dados estão corretos e tente novamente!')

    context = {}
    return render(request, 'Pessoa/cadastro.html', context)

# @login_required
def area_restrita(request):
    # Recuperando todas as vagas disponíveis
    vagas = {}
    pessoas = {}
    
    todas_vagas = requests.get('http://127.0.0.1:8000/api/vagas/')

    if todas_vagas.status_code in [200, 201]:
        vagas = todas_vagas.json()

    #Recuperando todas as pessoas cadastradas
    
    todas_pessoas = requests.get('http://127.0.0.1:8000/api/pessoas/')

    if todas_pessoas.status_code in [200, 201]:
        pessoas = todas_pessoas.json()

    form = UploadForm()
    pessoa = request.user.pessoa.first()
    
    if request.POST:

        # Cadastro de vagas
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        requisitos = request.POST.get("requisitos")

        payload = {
                'titulo': titulo, 
                'descricao': descricao, 
                'requisitos': requisitos,
                'disponivel': True
        }

        cad_vagas = requests.post('http://127.0.0.1:8000/api/vagas/',data=payload)

        if cad_vagas.status_code in [200, 201]:
            messages.success(request, 'Cadastro realizado com sucesso')
        else:
            messages.error(request, 'Ocorreu um erro, verifique se os dados estão corretos e tente novamente!')

        # Cadastro de curriculo
        if request.FILES:
            arquivo = request.FILES.get('arquivo')
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                Curriculum.objects.get_or_create(pessoa = pessoa, anexo = arquivo.read())
    
    context = {
        'pessoa': pessoa,
        'form': form,
        'user': request.user,
        'vagas': vagas,
        'pessoas': pessoas
    }
    return render(request, 'Pessoa/area-restrita.html', context)
