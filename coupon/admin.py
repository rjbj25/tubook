from django.contrib import admin
from coupon.models import Coupon
# Register your models here.
@admin.register(Coupon)
class OrderAdmin(admin.ModelAdmin):
    list_display=('code', 'valid_from', 'valid_to', 'discount', 'active')

    search_fields = (
        'code',
        'valid_from', 
        'valid_to', 
        'discount'
    )
    list_filter = (
        'active',
    )