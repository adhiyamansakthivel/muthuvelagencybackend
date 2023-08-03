from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ExportActionMixin

from .models import *



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    list_display = ('name','brand', 'category', 'subcategory','status', 'created_at')

    list_filter = [
         "brand",
         "category",
         "subcategory",
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
    )

    class Meta:
        model = Product


class BrandAdmin(admin.ModelAdmin):
    list_filter = [
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
    )

    class Meta:
        model = Brand


class CategoryAdmin(admin.ModelAdmin):
    list_filter = [
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
    )
    class Meta:
        model = Category


# Register your models here.
admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCategory)
admin.site.register(ProductUsage)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)