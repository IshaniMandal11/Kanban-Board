from django.contrib import admin
from .models import Column, Task


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'column', 'created_at']
    list_filter = ['column']
