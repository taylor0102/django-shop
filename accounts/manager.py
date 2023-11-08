from django.contrib.auth.models import BaseUserManager, UserManager
from django.db import models
from django.db.models.query import QuerySet
    
    
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, mobile_phone, password=None):
        if not email:
            raise ValueError('email must be set')
        if not first_name:
            raise ValueError('first name must be set')
        if not last_name:
            raise ValueError('last name must be set')
        if not mobile_phone:
            raise ValueError('mobile phone must be set')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile_phone=mobile_phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, mobile_phone, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            mobile_phone=mobile_phone,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

