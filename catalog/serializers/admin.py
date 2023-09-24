from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from catalog.models import Category


class CategoryNodeCreateSerializer(serializers.ModelSerializer):
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


class CategoryTreeListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        res = CategoryTreeListSerializer(obj.get_children(), many=True).data
        return res

    class Meta:
        model = Category
        fields = ["id", "title", "description", "is_public", "slug", "children"]


CategoryTreeListSerializer.get_children = extend_schema_field(
    serializers.ListField(child=CategoryTreeListSerializer()))(
    CategoryTreeListSerializer.get_children
)


class CategoryNodeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
