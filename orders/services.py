import environ, requests, base64

from rest_framework import status
from rest_framework.response import Response

from users.services import UserEmailNotificationService
from . import models, serializers

env = environ.Env()

class OrderService:
    @staticmethod
    def create_new_order(request):
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.save()
            
            user_subject = "Λάβαμε την παραγγελία σου!"
            UserEmailNotificationService.send_user_email_template(
                template_name="user_new_order_created",
                subject=user_subject,
                receiving_address=[{"email": order.user.email}]
            )

            admin_subject = "Παραγγελία %s - %s - Εκκρεμεί" % (order.id, order.user.email)
            UserEmailNotificationService.send_admin_email_template(
                template_name="admin_new_order_created",
                subject=admin_subject,
            )

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
