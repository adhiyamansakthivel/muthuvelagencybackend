from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *




class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarsoulSerializer
    http_method_names = ['get']
# Create your views here.
