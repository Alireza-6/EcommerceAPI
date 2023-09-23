from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from catalog.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)

    def create(self, validated_data):
        parent = validated_data.pop('parent', None)
        if parent is None:
            instance = Category.add_root(**validated_data)
        else:
            parent_node = get_object_or_404(Category, pk=parent)
            instance = parent_node.add_child(**validated_data)
        return instance

    class Meta:
        model = Category
        fields = ["id", "title", "description", "is_public", "slug", "parent"]