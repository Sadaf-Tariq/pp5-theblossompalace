from django.contrib import admin
from .models import Type, FlowerCount, Product, Rating


admin.site.register(Product)
admin.site.register(Type)
admin.site.register(FlowerCount)
admin.site.register(Rating)