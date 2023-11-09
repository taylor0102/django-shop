from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category


@admin.register(Category)
class CategpryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    prepopulated_fields = {
        'slug': ('title', )
    }
