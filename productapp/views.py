from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse

# Create your views here.

@api_view(['GET'])
def getProducts(self):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# brand group start
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.filter(status=True)
    serializer_class = BrandSerializer
    lookup_field = 'brand_url'
    http_method_names = ['get']

class BrandCategoryViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.filter(status=True)
    serializer_class = BrandCategoryViewSerializer
    lookup_field = 'brand_url'
    http_method_names = ['get']

class BrandProductViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.filter(status=True)
    serializer_class = BrandProductViewSerializer
    lookup_field = 'brand_url'
    http_method_names = ['get']

# brand group end


# category group start
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySerializer
    lookup_field = 'category_url'
    http_method_names = ['get']

class CategoryBrandViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategoryBrandSerializer
    lookup_field = 'category_url'
    http_method_names = ['get']

class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategoryProductSerializer
    lookup_field = 'category_url'
    http_method_names = ['get']

# category group end

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


class ProductfilterViewSet(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        product_id = self.request.query_params.get('product_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if product_id and category_id: 
            queryset=queryset.filter(category=category_id).exclude(id=product_id)

        serializer_class = ProductSerializer(queryset, many=True)
        return Response(serializer_class.data)


class DivisionList(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, format=None):
        brand=request.data['data']
        division = {}
        if brand:
            divisions = Brand.objects.get(id=brand).divisions.all()
            division={p.name:p.id for p in divisions}
        return JsonResponse(data=division, safe=False)



class CategorySubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySubCategorySerializer
    lookup_field = 'category_url'
    http_method_names = ['get']


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.filter(status=True)
    serializer_class = SubCategoryViewSerializer
    lookup_field =  'subcategory_url'
    http_method_names = ['get']