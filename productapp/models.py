from django.db import models
import uuid
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
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
    


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.TextField(null=True, blank=True)

    avatar = models.ImageField(null=True, default="avatar.png", upload_to=RandomFileName('user_image'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    brand_url = AutoSlugField(populate_from ='name', unique=True, null=False, default=None)
    logo = models.ImageField(null=False, blank=False, upload_to=RandomFileName('brand_logo'), validators=[validate_file_size])
    website = models.URLField(null=True, blank=True)
    meta_title = models.CharField(max_length=200,  null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
       return self.name
    



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category_url = AutoSlugField(populate_from ='name', unique=True, null=False, blank=False, default=None)
    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
       return self.name
    
    

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory_url = AutoSlugField(populate_from ='name', unique=True, null=False, blank=False, default=None)
    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.meta_title = self.name
        super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
       return self.name
    
    



class ProductUsage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Use'

    def __str__(self):
       return self.name




   


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=200, null=False)
    image =  models.ImageField(null=True, blank=True, upload_to=RandomFileName('products'), validators=[validate_file_size])
    description = RichTextField(null=True, blank=True)
    product_url = AutoSlugField(populate_from ='name', unique=True, null=False, blank=False, default=None)
    product_use = models.ManyToManyField(ProductUsage, related_name='productuse', blank=True)
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
        super(Product, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
       return self.name + ": ₹" + str(self.price)
    



class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productImages')
    product_Image = models.ImageField(upload_to=RandomFileName('productlist'),  null=False , validators=[validate_file_size])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'product Images'

 