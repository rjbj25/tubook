from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=60, null=False)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    neighborhood = models.CharField(max_length=60)
    zip_code = models.IntegerField()
    aditional_reference = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return Username"""
        return self.user.username

