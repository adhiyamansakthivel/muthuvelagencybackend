from django.db import models
import uuid

# Create your models here.
class Carousel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=False, blank=False, upload_to="carousel/")
    description = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title