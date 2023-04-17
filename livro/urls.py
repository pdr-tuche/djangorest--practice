from rest_framework import routers
from livro.views import LivroViewSet,LivrariaViewSet
from django.urls import path, include
from .exportCSV import exporta_livros_csv

router = routers.DefaultRouter()

router.register('livros', LivroViewSet)
router.register('livrarias', LivrariaViewSet)

urlpatterns = [
    path('exportar-livros-csv/', exporta_livros_csv, name='exportar_receitas_csv'),
    path('',include(router.urls)),
    ]
