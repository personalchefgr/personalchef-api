from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .services import PostcodeAreaService


class PostcodeAreaList(APIView):
    permission_classes = []

    def get(self, request):
        response = PostcodeAreaService.get_postcode_area_by_postcode(request)

        return response


class PostcodeAreaDetails(APIView):
    permission_classes = []

    def get(self, request, postcode):
        response = PostcodeAreaService.get_postcode_area_by_postcode(postcode)

        return response

