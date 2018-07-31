from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['status', 'name', 'phone', 'promo', 'created', 'updated', 'note']
    list_display_links = ('name',)

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)
