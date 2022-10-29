from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from stageoneapiapp.models import apidata

class apidataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = apidata
        fields = ('slackUsername', 'backend', 'age', 'bio')