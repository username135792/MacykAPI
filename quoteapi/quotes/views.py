from django.shortcuts import render
from rest_framework import viewsets
from .models import Theme, Quote
from .serializers import ThemeSerializer, QuoteSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    
    def get_queryset(self):
        queryset = Quote.objects.all()
        theme = self.request.query_params.get('theme', None)
        if theme is not None:
            queryset = queryset.filter(themes__name__icontains=theme)
        return queryset