from django.contrib import admin

# Register your models here.
from .models import Branch, Appointment, Customer, StaffMember

admin.site.register(Branch)
admin.site.register(Appointment)
admin.site.register(StaffMember)
admin.site.register(Customer)