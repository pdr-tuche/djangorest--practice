from django.db import models
from rest_framework import serializers

class Livro(models.Model):
    titulo = models.CharField(max_length=120)
    numero_paginas = models.IntegerField()
    autor = models.CharField(max_length=120)

    def __str__(self):
        return 'titulo: {},autor: {}, numero de paginas: {}'.format(self.titulo, self.numero_paginas, self.autor)

class Livraria(models.Model):
    nome = models.CharField(max_length=120)
    livros = models.ForeignKey(Livro, on_delete=models.CASCADE)
    scores = serializers.ListField(
        child=serializers.
    )

    def __str__(self):
        return 'nome: Livraria {}'.format(self.nome)