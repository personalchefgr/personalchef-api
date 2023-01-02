from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from . import services

class PostcodeAreaDetails(APIView):
    persmission_classes = []
    
    def get(self, request, postcode):
        if postcode:
            postcode_area = services.PostcodeAreaService.get_postcode_area_by_postcode(postcode)

            return Response(postcode_area, status=HTTP_200_OK)

        return Response(status=HTTP_400_BAD_REQUEST)