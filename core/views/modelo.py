from rest_framework.viewsets import ModelViewSet

from core.models import modelo
from core.serializers import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = modelo.objects.all()
    serializer_class = ModeloSerializer
