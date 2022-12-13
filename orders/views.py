from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import OrderService

class NewOrderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        response = OrderService.create_new_order(request)

        return response