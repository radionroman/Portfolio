from django.contrib import admin

# Register your models here.
from .models import Project, Screenshots

admin.site.register(Project)
admin.site.register(Screenshots)