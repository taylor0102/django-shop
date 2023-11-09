from rest_framework import serializers
from Category import models


class CategorySerialziers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
