from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Models
from apps.core.models import Person
# Serializers
from . import serializers


class PersonAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = Person.objects.all()
        serializer = serializers.PersonSerializer(
            queryset, context={"request": request},
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    