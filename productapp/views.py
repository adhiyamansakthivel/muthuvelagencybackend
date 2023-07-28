from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

@api_view(['GET'])
def getProducts(self):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.filter(status=True)
    serializer_class = BrandViewSerializer
    lookup_field = 'brand_url'
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True).prefetch_related('products').filter(products__status=True)
    serializer_class = CategoryViewSerializer
    lookup_field = 'category_url'
    http_method_names = ['get']

class ProductUsageViewSet(viewsets.ModelViewSet):
    queryset = ProductUsage.objects.all()
    serializer_class = ProductUsageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(status=True).select_related('brand').filter(brand__status=True).select_related('category').filter(category__status=True)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["brand", "category"]
    search_fields = ["name"]
    lookup_field = 'product_url'
    http_method_names = ['get']


    
class AllInViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all(), Category.objects.all() , Brand.objects.all()
    serializer_class = ProductSerializer


