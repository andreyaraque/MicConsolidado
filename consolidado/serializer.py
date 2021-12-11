from rest_framework import serializers
from .models import *

class ConsolidadoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Consolidado
        fields=['ciudad','id','total_ventas']