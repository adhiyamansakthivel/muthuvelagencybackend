from django.contrib import admin


from .models import Carousel
# Register your models here.

MAX_OBJECTS = 6


class CarouselAdmin( admin.ModelAdmin):

    list_display = ('title', 'status', 'created_at')

    list_filter = [
        'status',
        'created_at'
    ]
    search_fields = (
        "name",
    )

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)
    class Meta:
        model = Carousel



admin.site.register(Carousel, CarouselAdmin)
