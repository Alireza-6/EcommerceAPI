from rest_framework import viewsets

from catalog.models import Category
from catalog.serializers.admin import CategoryNodeCreateSerializer, CategoryTreeSerializer


class CategoryView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryTreeSerializer
        else:
            return CategoryNodeCreateSerializer
