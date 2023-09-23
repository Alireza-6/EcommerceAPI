from rest_framework import viewsets

from catalog.models import Category
from catalog.serializers.admin import CategoryCreateSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
