import csv
from django.http import HttpResponse
from .models import Livro

def exporta_livros_csv (request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="livros.csv"'
    writer = csv.writer(response)
    writer.writerow(['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'])
    livros = Livro.objects.all()
    for livro in livros:
        writer.writerow([livro.titulo, livro.numero_paginas, livro.autor])
    return response