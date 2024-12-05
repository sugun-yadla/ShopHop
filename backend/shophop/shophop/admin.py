from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, SavedItem, productData

admin.site.register(User, UserAdmin)
admin.site.register(Product )
admin.site.register(SavedItem)
admin.site.register(productData)