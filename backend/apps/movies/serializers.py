from .models import movies
from rest_framework import serializers

class moviesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)
    class Meta:
        model = movies
        fields = '__all__'
    
