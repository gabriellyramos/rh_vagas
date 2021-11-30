from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as logar
from django.contrib import messages
import requests

from django.contrib.auth import logout

def login(request):
    if request.POST:
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        payload = {'username': usuario, 'password': senha}
        
        token = requests.post('http://127.0.0.1:8000/api/token/',data=payload)
        user_get = User.objects.filter(username = usuario)
        if len(user_get) > 0:
            user_get = user_get[0]
            user_get.set_password(senha)
            user_get.save()
        else:
            messages.error(request, 'Erro ao acessar, verifique se os dados estão corretos e tente novamente!')
        if token.status_code in [200, 201]:
            user = authenticate(request, username=usuario, password=senha)
            logar(request, user)
            return redirect(reverse('Pessoa:area_restrita'))
        else:
            messages.error(request, 'Erro ao acessar, verifique se os dados estão corretos e tente novamente!')
    context = {}
    return render(request, 'login.html', context)

def logout(request):
    logout(request)
    return redirect(reverse('login'))