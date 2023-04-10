from rest_framework import serializers
from livro.models import Livro, Livraria

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivrariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraria
        fields = ['id', 'nome', 'livro']
        depth=0
