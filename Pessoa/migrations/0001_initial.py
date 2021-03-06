# Generated by Django 3.2 on 2021-11-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=30, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.IntegerField(choices=[(0, 'Não binário'), (1, 'Feminino'), (2, 'Masculino')], default=0)),
                ('telefone', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
