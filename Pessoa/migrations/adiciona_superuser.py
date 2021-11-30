from django.db import migrations
from django.contrib.auth.models import User

def forward(apps, schema_editor):
    print(">>>>>>Adicionando super usuario")
    user = User()
    user.username = 'administrador'
    user.password = 'sovocesabe'
    user.set_password = 'sovocesabe'
    user.is_active = True
    user.is_staff = True
    user.is_superuser = True
    user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', 'adiciona_pessoa'),
    ]

    operations = [
        migrations.RunPython(forward)
    ]
