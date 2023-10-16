from django.db import models
import uuid
from autoslug import AutoSlugField
from django.contrib.auth.models import BaseUserManager, AbstractUser,  PermissionsMixin
import os
from django.utils.deconstruct import deconstructible
from ckeditor.fields import RichTextField
from galleryapp.validators import validate_file_size
from django.core.validators import RegexValidator
import random


# Create your models here.




@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)
    
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
             **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser,  PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.TextField(null=True, blank=True)

    avatar = models.ImageField(null=True, default="avatar.png", upload_to=RandomFileName('user_image'))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email


    @property
    def is_is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff

    @property
    def is_is_admin(self):
        "Is the user a admin member?"
        return self.is_admin





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
    

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    brand_url = AutoSlugField(populate_from ='name', unique=True, null=False, default=None)
    category = models.ManyToManyField(Category, related_name="brand")
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

    
    

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
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
    product_id = models.CharField(unique=True,blank=True, null=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
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
        self.product_id = random.randrange(1111111111, 9999999999, 10)
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

 