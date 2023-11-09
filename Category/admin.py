from django.contrib import admin
from treebeard.admin import TreeAdmin
from . import models


@admin.register(models.Category)
class CategpryAdmin(TreeAdmin):
    pass