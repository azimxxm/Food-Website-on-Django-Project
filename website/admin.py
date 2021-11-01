from django.contrib import admin
from .models import *


@admin.register(Our_Specialty)
class Our_SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'data_created']


@admin.register(Orders)
class OrdersyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price_1', 'price_2', 'data_created']


@admin.register(Gallarey)
class OrdersyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'data_created']

@admin.register(Received_Orders)
class OrdersyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone',  'is_published', 'data_created']

@admin.register(Comments)
class OrdersyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_published', 'data_created']