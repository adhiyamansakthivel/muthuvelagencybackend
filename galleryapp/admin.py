from django.contrib import admin
from .models import *



class GalleryAdmin(admin.ModelAdmin):
    list_filter = [
         'created_at'
    ]
    search_fields = (
        "name",
    )
    class Meta:
        model = Gallery
# Register your models here.
admin.site.register(Gallery, GalleryAdmin)
