from django.urls import path, include
from . import views
from rest_framework import routers
from productapp.views import *
router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)
router.register(r'brand',BrandViewSet)
router.register(r'brand_category', BrandCategoryViewSet)
router.register(r'brand_products', BrandProductViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'category_brand',CategoryBrandViewSet)
router.register(r'category_products',CategoryProductViewSet)
router.register(r'category_subcategories',CategorySubCategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)



# router.register(r'allview', AllInViewSet, basename='allinone')


urlpatterns = [
    path('', include(router.urls)),
    path('related_products', views.ProductfilterViewSet.as_view()),
    path('divisions/', views.DivisionList.as_view())
    
    # path('',  views.getProducts),

]