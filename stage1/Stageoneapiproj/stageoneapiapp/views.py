from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import apidataSerializer
from .models import apidata


@api_view(['GET'])
def getData(request):
    apidatas = apidata.objects.all()[0]
    serializer = apidataSerializer(apidatas)
    return Response(serializer.data)