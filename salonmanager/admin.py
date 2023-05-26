from django.contrib import admin

# Register your models here.
from .models import Package,Product,Service
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Package)
admin.site.register(Product)
admin.site.register(Service)
