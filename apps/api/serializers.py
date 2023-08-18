from rest_framework import serializers
from apps.api.models import Solicitudes

class SolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitudes
        fields = '__all__'
