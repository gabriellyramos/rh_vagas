# Generated by Django 3.2 on 2021-11-27 15:50

import Curriculum.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0002_curriculum_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to=Curriculum.models.path_curriculum),
        ),
    ]
