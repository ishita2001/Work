from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Category

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Category)


# Register your models here.
