from django.contrib import admin
from core.models import Task, Project, Log
# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Log)
