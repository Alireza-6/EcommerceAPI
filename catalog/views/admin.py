from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from catalog.models import Category
from catalog.serializers.admin import (
    CategoryNodeCreateSerializer,
    CategoryTreeListSerializer,
    CategoryNodeRetrieveSerializer,
    CategoryNodeUpdateDeleteSerializer,
)


class CategoryView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryTreeListSerializer
            case 'create':
                return CategoryNodeCreateSerializer
            case 'retrieve':
                return CategoryNodeRetrieveSerializer
            case 'update':
                return CategoryNodeUpdateDeleteSerializer
            case 'partial_update':
                return CategoryNodeUpdateDeleteSerializer
            case 'destroy':
                return CategoryNodeUpdateDeleteSerializer
            case _:
                raise NotAcceptable()
