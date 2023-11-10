from rest_framework import viewsets
from Category.models import Category
from . import serialziers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = serialziers.CategorySerialziers
