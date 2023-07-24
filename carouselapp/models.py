from django.db import models
import os
import uuid
from galleryapp.validators import validate_file_size
from django.utils.deconstruct import deconstructible


# Create your models here.
@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)

class Carousel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=False, blank=False,upload_to=RandomFileName('carousel'), validators=[validate_file_size])
    description = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title