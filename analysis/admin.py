from django.contrib import admin

# Register your models here.
from .models import FileUpload, Basic_stats, Advanced_analyis

admin.site.register(FileUpload)
admin.site.register(Basic_stats)
admin.site.register(Advanced_analyis)