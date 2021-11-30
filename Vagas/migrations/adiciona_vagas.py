from django.db import migrations
import requests

def forward(apps, schema_editor):
    print(">>>>>>Adicionando algumas vagas")

    vagas = [
        {
        'titulo': 'Desenvolvedor(a) Back-end Python Júnior (remoto)', 
        'descricao': 'Somos uma empresa startup que busca desenvolvedores para criar sistemas automatizados.', 
        'requisitos': 'Experiência em Django, em APIs.'
        },
        {
        'titulo': 'Desenvolvedor(a) em Angular (remoto)', 
        'descricao': 'Somos uma empresa que busca desenvolvedores para criar sistemas com o framework Angular.', 
        'requisitos': 'Conhecimentos sólidos em Angular e Typescript.'
        },
        {
        'titulo': 'Desenvolvedor(a) em IONIC (remoto)', 
        'descricao': 'Somos uma equipe que busca desenvolvedores para criar aplicativos híbridos utilizando IONIC.', 
        'requisitos': 'Conhecimentos básicos em IONIC.'
        }
    ]
    

    for vaga in vagas:

        payload = {
            'titulo': vaga['titulo'], 
            'descricao': vaga['descricao'], 
            'requisitos': vaga['requisitos'],
            'disponivel': True
        }

        cad_vagas = requests.post('http://127.0.0.1:8000/api/vagas/',data=payload)

class Migration(migrations.Migration):

    dependencies = [
        ('Vagas', '0002_vagas_disponivel'),
    ]

    operations = [
        migrations.RunPython(forward)
    ]
