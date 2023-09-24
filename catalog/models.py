from django.db import models
from treebeard.mp_tree import MP_Node

from catalog.managers import CategoryQuerySet


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    slug = models.SlugField()
    is_public = models.BooleanField(default=True)

    objects = CategoryQuerySet.as_manager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
