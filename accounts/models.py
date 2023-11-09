from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.utils import timezone
from django.db.models import Manager
from . import manager
from common.models import SoftDelete

class User(AbstractBaseUser, PermissionsMixin, SoftDelete):
    email = models.EmailField(max_length=100,
                              unique=True)
    mobile_phone = models.CharField(_('شماره همراه'),
                                    unique=True,
                                    max_length=11)
    first_name = models.CharField(_('نام'),
                                  max_length=100)
    last_name = models.CharField(_('خانوادگی'),
                                 max_length=100)
    birth_day = jmodels.jDateTimeField(_('تاریخ تولد'),
                                       blank=True,
                                       null=True)
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    date_joined = jmodels.jDateTimeField(_("date joined"),
                                         null=True,
                                         blank=True,
                                         default=timezone.now())
    update_information = jmodels.jDateTimeField(
        _('update user'),
        auto_now=True,
    )
    
    class JobUser(models.TextChoices):
        sportman = 'sportman'
        historiology = 'historiology'
        socialـSciences = 'social Sciences'
        Reporter = 'Reporter'
        Lawyer = 'Lawyer'
        Engineering  = 'Engineering'
        Graphics = 'Graphics'
        Marketing ='marketing'
        Transportation = 'Transportation'
        Programming = 'Programming'
        Sales_Marketing = 'Sales & Marketing'
    job = models.CharField(
        choices=JobUser.choices,
        default=JobUser.sportman,
        max_length=20),
        
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'mobile_phone')

    objects = manager.UserManager()
    
# 
    class Meta:
        db_table = 'user'


class RecycleUser(User):
    deleted = Manager()
    
    class Meta:
        proxy = True