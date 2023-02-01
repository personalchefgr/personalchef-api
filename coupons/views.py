from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import CouponService

class CouponDetails(APIView):
    persmission_classes = [IsAuthenticated]
    
    def get(self, request):
        response = CouponService.validate_coupon(request)

        return response
