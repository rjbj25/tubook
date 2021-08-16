from django.contrib import admin
from features.models import Feature
# Register your models here.
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display=('feature', 'price', 'revenue_margin')

    search_fields = (
        'feature',
        'price',
        'revenue_margin'
    )
