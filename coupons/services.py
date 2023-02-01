from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

class CouponService:
    @staticmethod
    def get_coupon(code=None):
        try:
            return models.Coupon.objects.get(code=code.strip())
        except:
            return None
    
    @staticmethod
    def get_all_coupons_for_user(user=None):
        user_coupons =  models.CouponUser.objects.filter(user=user)
        return [item.coupon for item in user_coupons]
        
    @staticmethod
    def validate_coupon(request):
        code = request.query_params.get('code')
        user = request.user
        
        if code is not None:
            coupon = CouponService.get_coupon(code)
            
            if coupon is not None and user is not None:
                user_coupons = CouponService.get_all_coupons_for_user(user)
                
                if coupon in user_coupons:
                    return Response(
                        {"error": "Το κουπόνι έχει ήδη χρησιμοποιηθεί."}, 
                        status=status.HTTP_404_NOT_FOUND
                    )
                
                serializer = serializers.CouponSerializer(coupon)

                return Response({"data": serializer.data},
                    status=status.HTTP_200_OK
                )
            
            return Response(
                {"error": "Το κουπόνι δεν είναι έγκυρο."}, 
                status=status.HTTP_404_NOT_FOUND
            )
            
        return Response(
            {"error": "Κάτι πήγε στραβά."}, 
            status=status.HTTP_400_BAD_REQUEST
        )
