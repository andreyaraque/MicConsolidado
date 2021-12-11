from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from consolidado.serializer import ConsolidadoSerializers
from .models import *
# Create your views here.
class ConsolidadoViewSet(viewsets.ModelViewSet):
    queryset=Consolidado.objects.all()
    serializer_class=ConsolidadoSerializers