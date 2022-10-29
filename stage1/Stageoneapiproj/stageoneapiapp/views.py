from django.shortcuts import render
from rest_framework import routers, viewsets, serializers
from Stageoneapiproj.serializers import apidataSerializer
from stageoneapiapp.models import apidata

# Create your views here.

#viewsets
class apidataViewSet(viewsets.ModelViewSet):
    queryset = apidata.objects.all()
    serializer_class = apidataSerializer