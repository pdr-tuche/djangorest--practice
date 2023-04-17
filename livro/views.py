from rest_framework import viewsets, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter

from livro.models import Livro, Livraria
from livro.serializers import LivroSerializer, LivrariaSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['titulo'] #ordenação padrao
    filterset_fields = [ #especifica quais campos podem ser filtrados
        'titulo',
        'numero_paginas',
        'autor'
    ]

    ordering_fields = [ #especifica quais campos podem ser ordenados
        'titulo',
        'numero_paginas',
        'autor']

class LivrariaViewSet(viewsets.ModelViewSet):
    queryset = Livraria.objects.all()
    serializer_class = LivrariaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
