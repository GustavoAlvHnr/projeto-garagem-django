from rest_framework.viewsets import ModelViewSet

from core.models import acessorios
from core.serializers import AcessoriosSerializer


class AcessoriosViewSet(ModelViewSet):
    queryset = acessorios.objects.all()
    serializer_class = AcessoriosSerializer
