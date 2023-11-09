from django.contrib import admin
from treebeard.admin import TreeAdmin
from .models import Category


@admin.register(Category)
class CategpryAdmin(TreeAdmin):
    prepopulated_fields = {'slug': ('title',)}
