from django.contrib import admin
from task.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status")
    fields = ("name", "description", "status", 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Task, TaskAdmin)
