from rest_framework import serializers
from .models import titanic

class titanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = titanic
        fields = '__all__'





