from rest_framework import serializers
from . import  models


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'email',
            'mobile_phone',
            'password',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'password': {'write_only': True,},
        }
    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            mobile_phone=validated_data['mobile_phone'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            
        )
        return user



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = (
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'deleted_at',
            'is_deleted'
        )