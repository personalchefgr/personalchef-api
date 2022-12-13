from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

class OrderService:
    @staticmethod
    def create_new_order(request):
        serializer = serializers.NewOrderSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)