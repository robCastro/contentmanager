from rest_framework import serializers
from content.models import Archivo, Sistema


class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = ['id', 'nombre', 'descripcion']


class ArchivoSerializer(serializers.ModelSerializer):
    sistemas = SistemaSerializer(many=True)

    class Meta:
        model = Archivo
        fields = ['id', 'nombre', 'descripcion', 'sistemas']


