from rest_framework import generics
from .serializers import categorySerializer
from .models import category


class categoryList(generics.ListAPIView):
    queryset = category.objects.order_by('created_at').all()
    serializer_class = categorySerializer
