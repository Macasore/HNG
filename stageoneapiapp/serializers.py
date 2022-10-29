from rest_framework import serializers
from stageoneapiapp.models import apidata

class apidataSerializer(serializers.ModelSerializer):
    class Meta:
        model = apidata
        fields = ['slackUsername', 'backend', 'age', 'bio']