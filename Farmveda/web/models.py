from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10),RegexValidator(r'^\d{1,10}$')], default='')
    firm_name = models.CharField(max_length=100,default='')
    website = models.URLField(max_length=100,default='')

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , primary_key = True)
    #rating = 

class Category(models.Model):
    name = models.CharField(max_length = 50)

class Product(models.Model):
    name = models.CharField(max_length = 50)
    # category = models.CharField(max_length = 25)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products')
    price = models.IntegerField(blank=True)
    image = models.FileField()
    seller = models.ForeignKey(User, on_delete = models.CASCADE, related_name='products')
    #flag to differentiate crawled data from signed up data
    crawled = models.BooleanField(default=False)    
    rating = models.FloatField(default=0)
    quantity = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key = True)
    wishlist = models.ManyToManyField(Product)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.user.username)
