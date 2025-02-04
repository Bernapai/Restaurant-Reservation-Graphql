from django.contrib import admin
from .models import Restaurant, Table, Order

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Order)
