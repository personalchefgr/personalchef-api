from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import OrderService

class NewOrderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        response = OrderService.create_new_order(request)

        return response


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None):
        response = OrderService.get_order_by_id(id)

        return response
    

class OrderShippingDetailsView(APIView):
    permission_classes = []

    def get(self, request, id=None):
        response = OrderService.get_shipping_details(id)

        return response

    def post(self, request, id=None):
        response = OrderService.add_shipping_details(request)

        return response
    

class OrderBillingDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        response = OrderService.add_billing_details(request, id)

        return response
    

class OrderCompanyTaxDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        response = OrderService.add_company_tax_details(request, id)

        return response