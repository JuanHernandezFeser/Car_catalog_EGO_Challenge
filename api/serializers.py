from rest_framework import serializers
from .models import Car, Category, CarFeature

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'
        
class CarFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarFeature
        fields='__all__'

class CarSerializer(serializers.ModelSerializer):
    
    carfeature_set = CarFeatureSerializer(many=True, read_only=True)
    
    class Meta:
        model=Car
        fields = '__all__'