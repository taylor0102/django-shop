from rest_framework import serializers
from . import  models


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'email',
            'mobile_phone',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True,},
        }
    def create(self, validated_data):
        models.User.objects.bulk_create(
            email=validated_data['email'],
            mobile_phone=validated_data['mobile_phone'],
            password=validated_data['password'],
            
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'email',
            'mobile_phone',
            'first_name',
            'last_name',
            'birth_day',
            'date_joined',
        )