from django.urls import path, include
from rest_framework import routers
from carouselapp.views import CarouselViewSet 
router = routers.DefaultRouter()
router.register('', CarouselViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('',  views.getProducts),

]