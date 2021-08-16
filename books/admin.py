from django.contrib import admin
from books.models import Book

# Register your models here.
@admin.register(Book)
class OrderAdmin(admin.ModelAdmin):
    list_display=('format_form', 'cover_type', 'union_type', 'cover', 'have_sub_cover','sheets_quantity')

    search_fields = (
        'format_form', 
        'cover_type', 
        'union_type', 
        'cover'
    )
    list_filter = (
        'have_sub_cover',
        'sheets_quantity'
    )