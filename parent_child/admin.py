from django.contrib import admin
from django.contrib.auth.models import Group

# App models
from .models import *


# Override django admin panel default name
admin.site.site_header = "UDPlatforms Assignment Admin"

# Unregistering default Group class
admin.site.unregister(Group)


# Parent table customization for django admin panel
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip']
    list_display_links = ['first_name']
    list_filter = ['city', 'state', 'zip']
    search_fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip']
    ordering = ['id']


# Child table customization for django admin panel
@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'parent']
    list_display_links = ['first_name']
    list_filter = ['parent']
    search_fields = ['id', 'first_name', 'last_name', 'parent']
    ordering = ['id']


