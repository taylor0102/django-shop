from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from . import serialziers
from Category import models

class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return models.Category.objects.filter(depth=1)
        else:
            return models.Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return serialziers.CategroTreeNodesSerializers
            case 'create':
                return serialziers.CreateCategoryNodeSerialzier
            case 'retrieve':
                return serialziers.CategoryNodeRetriveSerialzier
            case 'update':
                return serialziers.CategoryUpdateSerialzier
            case 'partial_update':
                return serialziers.CategoryUpdateSerialzier
            case 'destroy':
                return serialziers.CategoryDeleteSerializers
            
            case _:
                raise NotAcceptable()