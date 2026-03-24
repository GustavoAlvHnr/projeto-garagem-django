from rest_framework.viewsets import ModelViewSet

from core.models import veiculo
from core.serializers import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = veiculo.objects.all()
    serializer_class = VeiculoSerializer
