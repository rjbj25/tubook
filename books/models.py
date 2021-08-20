from django.db import models
from django.db.models.enums import Choices
from features.models import Feature
# Create your models here.

class Book(models.Model):
    FORMAT_FORM = (
        ('10x20','Carta'),
        ('20x10','Libreta Pequeña'),
        ('20x30','Libreta Normal'),
    )
    COVER_TYPE = (
        ('10x20','Carta'),
        ('20x10','Libreta Pequeña'),
        ('20x30','Libreta Normal'),
    )
    UNION_TYPE = (
        ('10x20','Carta'),
        ('20x10','Libreta Pequeña'),
        ('20x30','Libreta Normal'),
    )
    SHEETS_QUANTITY = (
        (50,'50'),
        (80,'80'),
        (100,'100'),
        (200,'200'),
    )
    SHEETS_TYPE = (
        ('Papel Blond','Papel Blond'),
    )
    format_form = models.CharField(max_length=30, choices=FORMAT_FORM,verbose_name='Factor de Forma')
    cover_type = models.CharField(max_length=30, choices=COVER_TYPE, verbose_name='Tipo de Cubierta')
    union_type = models.CharField(max_length=30, choices=UNION_TYPE, verbose_name='TIPO DE UNION')
    cover = models.ImageField(upload_to='books/media/cover', verbose_name='Imagen de Cubierta')
    sub_cover = models.ImageField(upload_to='books/media/sub_cover', verbose_name='Imagen de Cubierta Interna')
    have_sub_cover = models.BooleanField(default=False, verbose_name='Agregar Cubierta Interna')
    sheets_quantity = models.CharField(max_length=20, choices=SHEETS_QUANTITY, verbose_name='Cantidad de Hojas')
    sheets_type = models.CharField(max_length=20, choices=SHEETS_TYPE, verbose_name='Tipo de Hoja Interna')
    
    def __str__(self) -> str:
        return self.format_form + ', ' + self.union_type + ', ' + self.cover_type

    def get_price(self):
        return (Feature.get_price(self.format_form) +
        Feature.get_price(self.cover_type) +
        Feature.get_price(self.union_type) +
        Feature.get_price(self.have_sub_cover) +
        (Feature.get_price(self.sheets_type)*self.sheets_quantity))