from django.contrib import admin
from .models import Product, Order,Project,Account

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Project)
admin.site.register(Account)
