from .models import category
from rest_framework import serializers

class categorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)
    class Meta:
        model = category
        fields = '__all__'
    
