from rest_framework import viewsets

from catalog.api.serializers import CategoryListSerializer
from catalog.models import Category


class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
