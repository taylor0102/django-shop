from rest_framework import serializers
from . import  models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'email',
            'mobile_phone',
            'first_name',
            'last_name',
            'is_active',
            'birth_day',
            'date_joined'
        )


class OtpCodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OtpCodeModel
        fields = (
            'email',
            'code',
            'created_at'
        )