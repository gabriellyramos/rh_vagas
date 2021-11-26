from Pessoa.models import Pessoa
from Vagas.models import Vagas
from .serializers import PessoasSerializer, VagasSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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

##### APIs para as vagas cadastradas #####
class VagasView(APIView):
    def get_object(self, pk):
        try:
            return Vagas.objects.get(pk=pk)
        except Vagas.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = Vagas.objects.all().order_by('id')
        serializer = VagasSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VagasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VagasDisponiveisView(APIView):
    def get_object(self, pk):
        try:
            return Vagas.objects.get(pk=pk)
        except Vagas.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = Vagas.objects.all().order_by('id')
        serializer = VagasSerializer(queryset, many=True)
        return Response(serializer.data)
