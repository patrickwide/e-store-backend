from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Shop)
admin.site.register(Notification)
admin.site.register(shoppingCache)
admin.site.register(Order)
