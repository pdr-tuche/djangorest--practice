from rest_framework import routers
from livro.views import LivroViewSet,LivrariaViewSet


router = routers.DefaultRouter()

router.register('livros', LivroViewSet)
router.register('livrarias', LivrariaViewSet)

urlpatterns = router.urls