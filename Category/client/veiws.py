from rest_framework import viewsets
from Category import models
from . import serialziers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serialziers.CategorySerialziers
