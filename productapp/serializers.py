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


class ProducCategoryViewSerializer(serializers.HyperlinkedModelSerializer):
    brand = BrandSerializer()
    subcategory = SubCategorySerializer()
    product_use = ProductUsageSerializer(many=True)
    productImages = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id','name','image','description', 'brand',
            'subcategory', 'product_use', 'product_url', 'price', 'quantity',
            'meta_title', 'meta_keywords', 'meta_description', 'productImages'
        ]
        


class CategoryBrandSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_url','brand', 'meta_title', 'meta_keywords','meta_description' ]
        lookup_field = 'category_url'
        extra_kwargs = {
            'url': {'lookup_field': 'category_url'}
        }




class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProducCategoryViewSerializer(many = True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_url','products', 'meta_title', 'meta_keywords','meta_description' ]
        lookup_field = 'category_url'
        extra_kwargs = {
            'url': {'lookup_field': 'category_url'}
        }


class ProducBrandViewSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    product_use = ProductUsageSerializer(many=True)
    productImages = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id','name','image','description', 
            'category', 'subcategory', 'product_use', 'product_url', 'price', 'quantity',
            'meta_title', 'meta_keywords', 'meta_description', 'productImages'
        ]
        


# class BrandViewSerializer(serializers.ModelSerializer):
#     category = CategoryViewSerializer(many=True)
#     class Meta:
#         model = Brand
#         fields = ['id', 'name', 'brand_url', 'logo', 'category','products',
#           'meta_title', 'meta_keywords', 'meta_description'
#         ]
#         lookup_field = 'brand_url'
#         extra_kwargs = {
#             'url': {'lookup_field': 'brand_url'}
#         }


class BrandCategoryViewSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Brand
        fields = ['id', 'name', 'brand_url', 'logo', 'category',
          'meta_title', 'meta_keywords', 'meta_description'
        ]

        lookup_field = 'brand_url'
        extra_kwargs = {
            'url': {'lookup_field': 'brand_url'}
        }

class BrandProductViewSerializer(serializers.ModelSerializer):
    products = ProducBrandViewSerializer(many=True)
    class Meta:
        model = Brand
        fields = ['id', 'name', 'brand_url', 'logo', 'products',
          'meta_title', 'meta_keywords', 'meta_description'
        ]

        lookup_field = 'brand_url'
        extra_kwargs = {
            'url': {'lookup_field': 'brand_url'}
        }






class CategorySubCategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_url','subcategory', 'meta_title', 'meta_keywords','meta_description' ]
        lookup_field = 'category_url', 
        extra_kwargs = {
            'url': {'lookup_field': 'category_url'}
        }




class SubCategoryViewSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    products = ProducCategoryViewSerializer(many = True)


    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'subcategory_url', 'category', 'products',  'meta_title', 'meta_keywords','meta_description' ]
        lookup_field = 'subcategory_url'
        extra_kwargs = {
            'url': {'lookup_field':  'subcategory_url'}
        }
        

class SubCategoryProductViewSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    products = ProducCategoryViewSerializer(many = True)


    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'subcategory_url', 'category', 'products', 'meta_title', 'meta_keywords','meta_description' ]
        lookup_field = 'subcategory_url'
        extra_kwargs = {
            'url': {'lookup_field':  'subcategory_url'}
        }
        



