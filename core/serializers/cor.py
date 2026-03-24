from rest_framework.serializers import ModelSerializer

from core.models import cor


class CorSerializer(ModelSerializer):
    class Meta:
        model = cor
        fields = '__all__'
