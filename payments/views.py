from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import PaymentService

class PaymentOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        _access_token = \
                PaymentService.viva_wallet_OAuth2_access_token()

        response = PaymentService.get_order_code(
                        request, order_id, _access_token)

        return response


class VerifyTransactionVIew(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        _access_token = PaymentService.viva_wallet_OAuth2_access_token()
        response = PaymentService.verify_transaction(request, _access_token)

        return response


class ConfirmPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = PaymentService.confirm_payment(request)

        return response