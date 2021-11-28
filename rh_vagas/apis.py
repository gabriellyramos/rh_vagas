from Pessoa.models import Pessoa
from Vagas.models import Vagas
from .serializers import PessoasSerializer, VagasSerializer, UsuarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User

from rh_vagas import serializers

##### APIs para as pessoas cadastradas #####
class PessoasView(APIView):
    # permission_classes = (IsAuthenticated,)  

    def get_object(self, pk):
        try:
            return Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = Pessoa.objects.all().order_by('id')
        serializer = PessoasSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PessoasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioView(APIView):
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

            user = User.objects.get(username = request.data['username'])
            serializer = UsuarioSerializer(user, data=request.data)
            if serializer.is_valid():
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'username': user.username,
                    'email': user.email
                })

##### APIs para as vagas cadastradas #####
class VagasView(APIView):
    def get_object(self, pk):
        try:
            return Vagas.objects.get(pk=pk)
        except Vagas.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = Vagas.objects.filter(disponivel=True).order_by('id')
        serializer = VagasSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VagasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

