from urllib.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from . import serializers
from . import models
import random


class UserViewSet(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class OtpCodeApiview(APIView):
    serializer_class = serializers.OtpCodeSerializers
    def get(self, request: Request):
        ser_data = self.serializer_class()
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        pass
