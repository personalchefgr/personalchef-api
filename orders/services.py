import environ, requests, base64

from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

env = environ.Env()

class OrderService:
    @staticmethod
    def create_new_order(request):
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
