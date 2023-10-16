from django.db import models
import uuid
from autoslug import AutoSlugField
from productapp.models import Category
import os
from django.utils.deconstruct import deconstructible
from ckeditor.fields import RichTextField
from galleryapp.validators import validate_file_size
# Create your models here.




@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)
    




class EkCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    pcategory_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Product Category", related_name='ekcategories')
    ecategory_url = AutoSlugField(populate_from ='name', unique=True, null=False, blank=False, default=None)
    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(EkCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ekart Category'
        verbose_name_plural = 'Ekart Categories'

    def __str__(self):
       return self.name
    



class EkBrand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    brand_url = AutoSlugField(populate_from ='name', unique=True, null=False, default=None)
    category = models.ManyToManyField(EkCategory, related_name="brand")
    logo = models.ImageField(null=False, blank=False, upload_to=RandomFileName('Ekart_brand_logo'), validators=[validate_file_size])
    website = models.URLField(null=True, blank=True)
    meta_title = models.CharField(max_length=200,  null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(EkBrand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ekart Brand'
        verbose_name_plural = 'Ekart Brands'

    def __str__(self):
       return self.name

    



class EkSubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    ecategory = models.ForeignKey(EkCategory, on_delete=models.CASCADE, related_name="eksubcategory")
    esubcategory_url = AutoSlugField(populate_from ='name', unique=True, null=False, blank=False, default=None)
    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(EkSubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ekart Category'
        verbose_name_plural = 'Ekart Sub Categories'

    def __str__(self):
       return self.name
    


class EkProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(EkBrand, on_delete=models.CASCADE, related_name='ekart_products')
    category = models.ForeignKey(EkCategory, on_delete=models.CASCADE, related_name='ekart_products')
    subcategory = models.ForeignKey(EkSubCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='ekart_products')
    name = models.CharField(max_length=200, null=False)
    image =  models.ImageField(null=True, blank=True, upload_to=RandomFileName('ekart_products'), validators=[validate_file_size])
    description = RichTextField(null=True, blank=True)
    product_url = AutoSlugField(populate_from ='name', unique=True, null=False, blank=False, default=None)
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200,  null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True,  blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(EkProduct, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Ekart Product'
        verbose_name_plural = 'Ekart products'

    def __str__(self):
       return self.name + ": ₹" + str(self.price)
    



class EkProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(EkProduct, on_delete=models.CASCADE, related_name='ekart_productImages')
    product_Image = models.ImageField(upload_to=RandomFileName('ekart_productlist'),  null=False , validators=[validate_file_size])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ekart Product Image'
        verbose_name_plural = 'Ekart Product Images'

 