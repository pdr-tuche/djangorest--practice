from django.db import models
from rest_framework import serializers


class Livro(models.Model):
    titulo = models.CharField(max_length=120)
    numero_paginas = models.IntegerField()
    autor = models.CharField(max_length=120)

    def __str__(self):
        return '{} - {}'.format(self.titulo, self.autor)


class Livraria(models.Model):
    nome = models.CharField(max_length=120)
    livro = models.ManyToManyField(Livro, related_name="livro")

    def __str__(self):
        return self.nome
