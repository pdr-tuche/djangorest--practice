from django.shortcuts import render
from rest_framework import viewsets
from livro.models import Livro, Livraria
from livro.serializers import LivroSerializer, LivrariaSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivrariaViewSet(viewsets.ModelViewSet):
    queryset = Livraria.objects.all()
    serializer_class = LivrariaSerializer

   # def create(self, request, *args, **kwargs):
    #    livraria_data = request.data
     #   nova_livraria = Livraria.objects.create(livros=Livro.objects.get(id=livraria_data['livros']), nome = livraria_data['nome'])