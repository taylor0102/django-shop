from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from django_jalali.admin.filters import JDateFieldListFilter
from . import models


@admin.register(models.User)
class UsersAdmin(UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "mobile_phone",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined",
                                           'update_information')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", 'mobile_phone', "password1", "password2"),
            },
        ),
    )
    list_display = ("mobile_phone", "email", "first_name", "last_name",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("mobile_phone", "first_name", "last_name", "email")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_display_links = ('mobile_phone', 'email')
    readonly_fields = ('update_information',)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return models.User.objects.filter(is_deleted=False)


@admin.register(models.RecycleUser)
class RecycleAdmin(admin.ModelAdmin):
    actions = ('recover',)
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return models.RecycleUser.deleted.filter(is_deleted=True)
    
    @admin.action(description='recovery user')
    def recover(self, request: HttpRequest, queryset: QuerySet[Any]):
        queryset.update(is_deleted=False, deleted_at=None)