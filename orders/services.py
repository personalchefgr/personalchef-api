import environ, requests, base64

from rest_framework import status
from rest_framework.response import Response

from users.services import UserEmailNotificationService
from coupons.services import CouponService
from . import models, serializers

env = environ.Env()

class OrderService:
    @staticmethod
    def get_order_by_id(id=None):
        try:
            order = models.Order.objects.get(pk=id)
            serializer = serializers.OrderSerializer(order)

            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        except:
            return Response({"error": "Η παραγγελία δεν βρέθηκε"},
                            status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def create_new_order(request):
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            # user_subject = "Λάβαμε την παραγγελία σου!"
            # UserEmailNotificationService.send_user_email_template(
            #     template_name="user_new_order_created",
            #     subject=user_subject,
            #     receiving_address=[{"email": order.user.email}]
            # )

            # admin_subject = "Παραγγελία %s - %s - Εκκρεμεί" % (order.id, order.user.email)
            # UserEmailNotificationService.send_admin_email_template(
            #     template_name="admin_new_order_created",
            #     subject=admin_subject,
            # )

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_shipping_details(id=None):
        try:
            order = models.Order.objects.get(pk=id)
            order_shipping_details = models.OrderShippingDetails.objects.get(order=order)
            serializer = serializers.OrderShippingDetailsSerializer(order_shipping_details)

            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        except:
            return Response({"error": "Η παραγγελία δεν βρέθηκε"},
                            status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def add_shipping_details(request):
        serializer = serializers.OrderShippingDetailsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        print(serializer.errors)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def add_billing_details(request, id=None):
        if id is not None:
            order_data = request.data
            order_data['order'] = id

            serializer = serializers.OrderBillingDetailsSerializer(data=order_data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
        return Response({"errors": "Δεν καταχωρήθηκε ο κωδικός παραγγελίας."}, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def add_company_tax_details(request, id=None):
        if id is not None:
            order_data = request.data
            order_data['order'] = id

            serializer = serializers.OrderCompanyTaxDetailsSerializer(data=order_data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
        return Response({"errors": "Δεν καταχωρήθηκε ο κωδικός παραγγελίας."}, status=status.HTTP_400_BAD_REQUEST)
    