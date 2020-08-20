from django.contrib import admin
from todo.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'is_doing')
    list_filter = ('date', 'task_name',)
    date_hierarchy = 'date'
    ordering = ('date', )
    search_field = ('task_name')

admin.site.register(Todo)