from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *




class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    http_method_names = ['get']