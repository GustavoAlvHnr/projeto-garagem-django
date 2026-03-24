from rest_framework.serializers import ModelSerializer

from core.models import modelo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = modelo
        fields = '__all__'
