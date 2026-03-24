from rest_framework.serializers import ModelSerializer

from core.models import acessorios


class AcessoriosSerializer(ModelSerializer):
    class Meta:
        model = acessorios
        fields = '__all__'
