from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from . import services

class SubscriptionList(APIView):
    def get(self, request):
        subscriptions = services.SubscriptionService.get_all_subscriptions()

        return Response(subscriptions, status=HTTP_200_OK)


class SubscriptionDetails(APIView):
    def get(self, request):
        return Response(status=HTTP_200_OK)