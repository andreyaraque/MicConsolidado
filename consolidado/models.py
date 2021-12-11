from django.db import models

# Create your models here.
class Consolidado (models.Model):
    ciudad=models.CharField(max_length=255,null=True)
    id=models.BigAutoField(primary_key=True)
    total_ventas=models.FloatField(null=True)