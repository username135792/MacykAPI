from rest_framework import serializers
from .models import Theme, Quote

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'name', 'description']

class QuoteSerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'source', 'themes', 'created_at', 'updated_at']