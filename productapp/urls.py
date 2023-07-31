from django.urls import path, include
from . import views
from rest_framework import routers
from productapp.views import ProductViewSet, BrandViewSet, CategoryViewSet, BrandCategoryViewSet, BrandProductViewSet, CategoryBrandViewSet, CategoryProductViewSet
router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)
router.register(r'brand',BrandViewSet)
router.register(r'brand_category', BrandCategoryViewSet)
router.register(r'brand_products', BrandProductViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'category_brand',CategoryBrandViewSet)
router.register(r'category_products',CategoryProductViewSet)


# router.register(r'allview', AllInViewSet, basename='allinone')


urlpatterns = [
    path('', include(router.urls)),
    # path('',  views.getProducts),

]