from rest_framework.views import APIView

from .services import NewsletterService

class PingAccountView(APIView):
    permission_classes = []

    def get(self, request):
        response = NewsletterService.ping_account()

        return response


class SubscribeView(APIView):
    permission_classes = []

    def post(self, request):
        response = NewsletterService.subscribe(request)

        return response