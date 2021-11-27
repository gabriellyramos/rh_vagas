from rest_framework import serializers
from Pessoa.models import Pessoa
from Vagas.models import Vagas
from django.contrib.auth.models import User

class PessoasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = '__all__'

class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'