from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .base_permission import IsSuperUser, IsOwner
from django.utils import timezone
from . import serializers
from . import models


class CreateUserApiView(CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    queryset = models.User.objects.all()


class ProfileUserViewSet(viewsets.ViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = models.User.objects.all
    permission_classes = (IsOwner,)
    

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset(), pk=pk)
        ser_user = self.serializer_class(user)
        return Response(ser_user.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset(), pk=pk)
        ser_user = self.serializer_class(user, data=request.data)
        if ser_user.is_valid():
            ser_user.save()
            return Response(ser_user.data, status=status.HTTP_201_CREATED)
        return Response(ser_user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset(), pk=pk)
        ser_user = self.serializer_class(user, data=request.data, partial=True)
        if ser_user.is_valid():
            ser_user.save()
            return Response(ser_user.data, status=status.HTTP_200_OK)
        return Response(ser_user.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset(), pk=pk)
        user.is_deleted = True
        user.is_active = False
        user.deleted_at = timezone.now()
        user.save()
        return Response({
            'messages': 'user has been deleted successfully'
        })



