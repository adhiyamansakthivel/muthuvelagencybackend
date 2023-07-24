from rest_framework import serializers
from .models import *


class CarsoulSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carousel
        fields = ['id', 'title', 'image', 'description' ]
    

    


