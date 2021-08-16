from django.db import models

# Create your models here.
class Feature(models.Model):
    feature = models.CharField(max_length=20)
    price = models.DecimalField()
    revenue_margin = models.DecimalField()

    def get_price(self,feat):
        element = self.objects.get(feature=feat)
        return element.price * element.revenue_margin

    def __str__(self) -> str:
        return self.feature