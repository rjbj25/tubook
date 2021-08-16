from django.db import models
from features.models import Feature
# Create your models here.

class Book(models.Model):
    format_form = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=30)
    union_type = models.CharField(max_length=30)
    cover = models.ImageField()
    sub_cover = models.ImageField()
    have_sub_cover = models.BooleanField(default=False)
    sheets_quantity = models.PositiveIntegerField()
    sheets_type = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.format_form + ', ' + self.union_type + ', ' + self.cover_type

    def get_price(self):
        return (Feature.get_price(self.format_form) +
        Feature.get_price(self.cover_type) +
        Feature.get_price(self.union_type) +
        Feature.get_price(self.have_sub_cover) +
        (Feature.get_price(self.sheets_type)*self.sheets_quantity))