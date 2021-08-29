from .models import Interno
from rest_framework import serializers


class InternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interno
        fields = '__all__'
