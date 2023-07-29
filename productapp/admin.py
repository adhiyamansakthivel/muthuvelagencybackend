from django.contrib import admin
from .models import *



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product


# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(SubCategory)
admin.site.register(ProductUsage)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)