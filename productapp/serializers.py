from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'brand_url', 'logo', 
          'meta_title', 'meta_keywords', 'meta_description'
        ]
        lookup_field = 'brand_url'
        extra_kwargs = {
            'url': {'lookup_field': 'brand_url'}
        }

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_url', 'meta_title', 'meta_keywords','meta_description' ]


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'subcategory_url', 'category', 'meta_title', 'meta_keywords','meta_description' ]



class ProductUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUsage
        fields = ['id', 'name']



class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'product_Image']



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    product_use = ProductUsageSerializer(many=True)
    productImages = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id','name','image','description', 'brand',
            'category', 'subcategory', 'product_use', 'product_url', 'price', 'quantity',
            'meta_title', 'meta_keywords', 'meta_description', 'productImages'
        ]
        lookup_field = 'product_url'
        extra_kwargs = {
            'url': {'lookup_field': 'product_url'}
        }









class CatNavSerilizerField(serializers.Field):
    def to_representation(self, category):

        if isinstance(category, (Category,)):
            category = category.id
        return category
    
    def to_internal_value(self, id):
        dict = {
            'category': Category.objects.get(pk=id)
        }
        return dict



class NavigationSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
   
    def get_category(self, obj):
        c = Category.objects.get(pk=obj['category'], many=True)

        return{
            'id':c.pk,
            'name': c.name,
        }
