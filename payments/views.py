from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import PaymentService

class PaymentOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = PaymentService.create_payment_order(request)

        return response