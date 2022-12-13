from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .services import SubscriptionService

class SubscriptionList(APIView):
    permission_classes = []

    def get(self, request):
        response = SubscriptionService.get_all()

        return response
