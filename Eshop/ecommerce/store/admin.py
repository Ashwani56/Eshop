from django.contrib import admin

# Register your models here.

from store.models import Category
from store.models import Customer
from store.models import Product

from store.models import Order

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

