# Generated by Django 3.2 on 2021-11-26 18:33

import Curriculum.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anexo', models.FileField(upload_to=Curriculum.models.path_curriculum)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curriculos', to='Pessoa.pessoa')),
            ],
        ),
    ]
