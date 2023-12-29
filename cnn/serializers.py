from rest_framework import serializers
from .models import tomato

class tomatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tomato
        fields = ['image']