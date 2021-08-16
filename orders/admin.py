from django.contrib import admin
from orders.models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('email', 'first_name', 'last_name', 'city', 'country', 'address')

    search_fields = (
        'email',
        'first_name',
        'last_name',
        'city',
        'country',
        'address',
        'paid'
    )
