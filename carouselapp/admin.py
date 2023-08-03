from django.contrib import admin


from .models import Carousel
# Register your models here.

class CarouselAdmin( admin.ModelAdmin):
    list_filter = [
        'status',
        'created_at'
    ]
    search_fields = (
        "name",
    )
    class Meta:
        model = Carousel
admin.site.register(Carousel, CarouselAdmin)
