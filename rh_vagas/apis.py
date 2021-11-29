from os import stat
from Curriculum.models import Curriculum
from Pessoa.models import Pessoa
from Vagas.models import Vagas
from .serializers import PessoasSerializer, VagasSerializer, UsuarioSerializer, CurriculumSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rh_vagas import serializers
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.exceptions import ParseError
from django.http import HttpResponse
import os

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
        if request.GET:
            queryset = Vagas.objects.filter(titulo__contains=request.GET['titulo']).order_by('id')
        else:
            queryset = Vagas.objects.filter(disponivel=True).order_by('id')
        serializer = VagasSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VagasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadCurriculum(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        pessoa = request.data['pessoa']
        file = request.FILES['file']
        pessoa = Pessoa.objects.get(id = int(pessoa))
        curriculum, criado = Curriculum.objects.get_or_create(
            pessoa = pessoa,
        )
        curriculum.anexo.save(file.name, file, save=True)
        curriculum.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, **kwargs):
        queryset = Curriculum.objects.filter(pessoa=request.GET['pessoa']).order_by('-id')
        serializer = CurriculumSerializer(queryset, many=True)
        return Response(serializer.data)

class CurriculumPDFView(APIView):
    # permission_classes = (IsAuthenticated,)       
    
    def get_object(self, pk):
        try:
            return Curriculum.objects.get(pk=pk)
        except Curriculum.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        curriculum = self.get_object(pk)
        
        with open(curriculum.anexo.path, 'rb') as fh:
            response = HttpResponse(
            fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + \
            os.path.basename(curriculum.anexo.name)
            return response