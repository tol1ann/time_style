from rest_framework import serializers
from .models import Category, Outfit, Thing

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OutfitSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Outfit
        fields = '__all__'

class ThingSerializer(serializers.ModelSerializer):
    outfit = OutfitSerializer(read_only=True)
    class Meta:
        model = Thing
        fields = '__all__'