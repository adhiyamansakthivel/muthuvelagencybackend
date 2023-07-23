from django.urls import path, include
from . import views
from rest_framework import routers
from productapp.views import ProductViewSet, BrandViewSet, NavigationViewSet 
router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('',  views.getProducts),

]