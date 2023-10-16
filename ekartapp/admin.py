from django.contrib import admin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from .models import *
from django.utils.html import format_html

# Register your models here.
class EkProductImageAdmin(admin.StackedInline):
    model = EkProductImage

class ProductResource(resources.ModelResource):
    brand = fields.Field(
        column_name='brand',
        attribute='brand',
        widget=ForeignKeyWidget(EkBrand, 'name'))
    
    category = fields.Field(
        column_name='ekart_category',
        attribute='ekart_category',
        widget=ForeignKeyWidget(EkCategory, 'name'))

    subcategory = fields.Field(
        column_name='',
        attribute='subcategory',
        widget=ForeignKeyWidget(EkSubCategory, 'name'))
    
    class Meta:
        fields = ('name','image', 'brand_name', 'category_name', 'subcategory_name','status', 'created_at')


class EkProductAdmin(admin.ModelAdmin):
    inlines = [EkProductImageAdmin]

    list_display = ('name','product_image', 'brand', 'category', 'subcategory','status', 'created_at')
    
    def product_image(self, obj):
        return format_html('<img src="{0}" width="auto" height="50px" >'
        .format(obj.image.url))

    
    resource_class = ProductResource

    list_filter = [
         "brand",
         "category",
         "subcategory",
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
        "product_id",
    )
    ordering = ['name', 'created_at']
    list_per_page = 15
    class Meta:
        model = EkProduct

# end product group

class EkBrandAdmin(admin.ModelAdmin):

    list_display = ('name','logo_image','status', 'created_at')

    def logo_image(self, obj):
        return format_html('<img src="{0}" width="auto" height="50px" >'
        .format(obj.logo.url))


    list_filter = [
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
    )

    class Meta:
        model = EkBrand


class EkCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')

    list_filter = [
         "status",
         'created_at'
    ]
    search_fields = (
        "name",
    )
    class Meta:
        model = Category


admin.site.register(EkCategory, EkCategoryAdmin)
admin.site.register(EkBrand, EkBrandAdmin)
admin.site.register(EkSubCategory)
admin.site.register(EkProduct, EkProductAdmin)
admin.site.register(EkProductImage)