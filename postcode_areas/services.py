from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

class PostcodeAreaService:
    @staticmethod
    def get_all():
        postcode_areas = models.PostcodeArea.objects.all()
        serializer = serializers.PostcodeAreaSerializer(postcode_areas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def get_postcode_area_by_postcode(postcode=None):
        if postcode is not None:
            try:
                postcode_area = models.PostcodeArea.objects.get(postcode=postcode)
                serializer = serializers.PostcodeAreaSerializer(postcode_area)

                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error": "No area found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"error": "No postcode submitted"}, status=status.HTTP_400_BAD_REQUEST)