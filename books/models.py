from django.db import models
# Create your models here.

class Book(models.Model):
    format_form = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=30)
    union_type = models.CharField(max_length=30)
    cover = models.ImageField()
    sheets_quantity = models.PositiveIntegerField()
    
    
    def __str__(self) -> str:
        return self.format_form + ', ' + self.union_type + ', ' + self.cover_type