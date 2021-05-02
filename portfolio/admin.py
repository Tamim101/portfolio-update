from django.contrib import admin
from .models import Product, Blog, Name

# Register your models here.

admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Name)