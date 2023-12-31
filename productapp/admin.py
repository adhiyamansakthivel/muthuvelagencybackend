from django.contrib import admin
from import_export.admin import  ExportMixin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
from django.utils.html import format_html


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'is_admin', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('bio', 'avatar')}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username',  'password1', 'password2', 'is_superuser', 'is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.



# product group
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductResource(resources.ModelResource):
    brand = fields.Field(
        column_name='brand',
        attribute='brand',
        widget=ForeignKeyWidget(Brand, 'name'))
    
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))

    subcategory = fields.Field(
        column_name='',
        attribute='subcategory',
        widget=ForeignKeyWidget(SubCategory, 'name'))
    
    class Meta:
        fields = ('name','image', 'brand_name', 'category_name', 'subcategory_name','status', 'created_at')


class ProductAdmin(ExportMixin, admin.ModelAdmin):
    inlines = [ProductImageAdmin]

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
        model = Product

# end product group

class BrandAdmin(admin.ModelAdmin):

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
        model = Brand


class CategoryAdmin(admin.ModelAdmin):
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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCategory)
admin.site.register(ProductUsage)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)