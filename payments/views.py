from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import PaymentService

class PaymentOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        PaymentService.print_request(request)
        _access_token = PaymentService.viva_wallet_OAuth2_access_token()
        response = PaymentService.create_payment_order(request, _access_token)

        return response