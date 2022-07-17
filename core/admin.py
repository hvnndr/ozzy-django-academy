from django.contrib import admin
from core import models

# Register your models here.

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_display_links = ['id', 'name', 'active', 'modified_at']
    search_fields = ['id', 'name', 'active']
    list_filter = ['active']

@admin.register(models.MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_display_links = ['id', 'name', 'active', 'modified_at']
    search_fields = ['id', 'name', 'active']
    list_filter = ['active']
    
