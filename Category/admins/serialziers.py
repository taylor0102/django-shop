from Category.models import Category
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from drf_spectacular.utils import extend_schema_field

class CreateCategoryNodeSerialzier(serializers.ModelSerializer):
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
        fields = (
            'id',
            'title',
            'slug',
            'is_public',
            'parent',
        )
        
    
class CategroTreeNodesSerializers(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    
    def get_children(self, obj):
        return CategroTreeNodesSerializers(obj.get_children(), many=True).data
    
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'is_public',
            'children'
        )
CategroTreeNodesSerializers.get_children = extend_schema_field(
    serializers.ListField(child=CategroTreeNodesSerializers())
)(CategroTreeNodesSerializers.get_children)


class CategoryNodeRetriveSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class CategoryUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'is_public',
        )
        

class CategoryDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'