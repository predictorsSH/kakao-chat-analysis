from django.contrib import admin

# Register your models here.
from .models import FileUpload, Basic_stats

admin.site.register(FileUpload)
admin.site.register(Basic_stats)