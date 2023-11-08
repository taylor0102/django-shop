from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.utils import timezone
from django.db.models import QuerySet, Manager, Q



class SofQueryset(QuerySet):
    def delete(self) -> tuple[int, dict[str, int]]:
        return self.update(is_deleted=True, deleted_at=timezone.now())


class SoftManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset(self.model, self._db).filter(
            Q(is_deleted=True) | Q(is_deleted__isnull=True)
        )


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        editable=False
    )
    deleted_at  = jmodels.jDateTimeField(
        null=True,
        blank=True,
        editable=False
    )
    objects = SoftManager()

    class Meta:
        abstract = True
    
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
        

# create model
class CreateModel(models.Model):
    created_at = jmodels.jDateTimeField(_('تاریخ ایجاد'),
                                     auto_now_add=True, editable=False)

    class Meta:
        abstract = True