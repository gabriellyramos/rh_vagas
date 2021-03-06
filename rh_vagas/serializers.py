from rest_framework import serializers
from Pessoa.models import Pessoa
from Vagas.models import Vagas
from django.contrib.auth.models import User
from Curriculum.models import Curriculum

class PessoasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = ('id','nome','sobrenome','data_nascimento','sexo','get_sexo_display','telefone','email','usuario')

class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields = ('id','titulo','descricao','requisitos','disponivel')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','is_active')

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('id','anexo','pessoa')