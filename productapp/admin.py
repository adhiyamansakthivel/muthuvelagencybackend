from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import *



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [ProductImageAdmin]

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


class BrandAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = [
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
    )

    class Meta:
        model = Brand


class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
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
admin.site.register(Category,)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCategory)
admin.site.register(ProductUsage)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)