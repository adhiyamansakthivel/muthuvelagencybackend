from django.urls import path, include
from rest_framework import routers
from galleryapp.views import GalleryViewSet 
router = routers.DefaultRouter()
router.register('', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('',  views.getProducts),

]