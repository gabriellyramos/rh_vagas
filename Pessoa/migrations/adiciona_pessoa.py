from django.db import migrations
import requests
import string
import random

def geraUsuario():
    qtde = 8
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(qtde))


def forward(apps, schema_editor):
    print(">>>>>>Adicionando primeiro os usuarios")

    pessoas = [{
        'nome': 'Gabrielly', 
        'sobrenome': 'Ramos', 
        'data_nascimento': '1994-06-08', 
        'telefone': '33988251093', 
        'sexo': 1, 
        'email': 'ybagramos@gmail.com'
    },{
        'nome': 'João', 
        'sobrenome': 'Barroso', 
        'data_nascimento': '1994-07-26', 
        'telefone': '33988251093', 
        'sexo': 2, 
        'email': 'joao@gmail.com'
    },
    {
        'nome': 'Maria', 
        'sobrenome': 'Lopes', 
        'data_nascimento': '1994-09-10', 
        'telefone': '33988251093', 
        'sexo': 0, 
        'email': 'maria@gmail.com'
    }]

    for pessoa in pessoas:

        codigo = geraUsuario()
        payload_user = {'username': codigo, 'password': codigo, 'email': pessoa['email'], 'is_active': True}
        cad_user = requests.post('http://127.0.0.1:8000/api/usuario/',data=payload_user)
        if cad_user.status_code in [200, 201]:
            retorno = cad_user.json()

            payload = {
                'nome': pessoa['nome'], 
                'sobrenome': pessoa['sobrenome'], 
                'data_nascimento': pessoa['data_nascimento'], 
                'telefone': pessoa['telefone'], 
                'sexo': pessoa['sexo'], 
                'email': pessoa['email'],
                'usuario': retorno.get("id")}
            
            cad_pessoa = requests.post('http://127.0.0.1:8000/api/pessoas/',data=payload)


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0002_pessoa_usuario'),
    ]

    operations = [
        migrations.RunPython(forward)
    ]
