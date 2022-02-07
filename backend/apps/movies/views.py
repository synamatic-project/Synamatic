from rest_framework import generics, filters
from .serializers import moviesSerializer
from .models import movies
from django_filters.rest_framework import DjangoFilterBackend

class moviesList(generics.ListAPIView):
    queryset = movies.objects.order_by('created_at').all()
    serializer_class = moviesSerializer
    filter_backend = [DjangoFilterBackend, filters.SearchFilters]
    filterset_fields = ['category_id', 'release_type']
    search_fields = ['name', 'description']