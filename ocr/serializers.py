from rest_framework import serializers
from .models import bill

class billSerializer(serializers.ModelSerializer):
    class Meta:
        model = bill
        fields = ['image']