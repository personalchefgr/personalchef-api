import environ, requests, base64

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from orders.models import Order
from users.models import CustomUser
from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription

env = environ.Env()

class PaymentService:
    @staticmethod
    def print_request(request):
        print(request.user)
        print(request.data)

    @staticmethod
    def viva_wallet_OAuth2_access_token():
        base_url = env('VIVA_WALLET_ACCOUNTS_URL')
        url = base_url + 'connect/token'

        client_id = env('VIVA_WALLET_CLIENT_ID')
        client_secret = env('VIVA_WALLET_CLIENT_SECRET')

        credentials = "%s:%s" % (client_id, client_secret)
        encoded_credentials = base64.b64encode(bytes(credentials, 'utf-8'))

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % encoded_credentials.decode('utf-8')
        }
        
        response = requests.post(url,
            headers=headers,
            data={'grant_type': 'client_credentials'}
        )

        if(response.status_code==200):
            data = response.json()
            return data['access_token']
        
        return None

    @staticmethod
    def get_order_code(
        request, 
        order_id=None, 
        _access_token=None
    ):
        order = get_object_or_404(Order, id=order_id)

        user = CustomUser.objects \
                .select_related('profile') \
                .get(id=order.user.id)
        dietary_plan = get_object_or_404(DietaryPlan, 
                    id=order.dietary_plan.id)
        subscription = get_object_or_404(Subscription, 
                    id=order.subscription.id)


        if _access_token is not None:
            base_url = env('VIVA_WALLET_API_URL')
            url = base_url + 'checkout/v2/orders'

            headers = {
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer %s' % _access_token
            }

            payload = {
                "customerTrns": "%s - %s" % (
                                dietary_plan, 
                                subscription
                            ),
                "customer": {
                    "email": user.email,
                    "fullName": "%s %s" % (
                        user.profile.first_name, 
                        user.profile.last_name
                    ),
                    "phone": user.profile.mobile_phone,
                    "countryCode": "GR",
                    "requestLang": "el-GR"
                },
                "amount": int(order.total_amount*100),
                "disableCash": "true",
                "disableWallet": "true",
                "merchantTrns": "%s - %s" % (
                                str(order.id), 
                                user.email
                            ),
                "sourceCode": \
                    env('VIVA_WALLET_PAYMENT_SOURCE_CODE'),
                
            }
            
            response = requests.post(url,
                headers=headers,
                json=payload,
            )

            if(response.status_code==200):
                return Response(response.json(), status=status.HTTP_200_OK)
            
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'Authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)
        

    @staticmethod
    def verify_transaction(request, _access_token):
        transaction_id = request.query_params.get('transaction_id')

        if transaction_id is not None and _access_token is not None:
            print(transaction_id)
            base_url = env('VIVA_WALLET_API_URL')
            url = base_url + '/checkout/v2/transactions/%s' % transaction_id

            headers = {
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer %s' % _access_token
            }

            response = requests.get(url,
                headers=headers,
            )

            if(response.status_code==200):
                return Response(response.json(), status=status.HTTP_200_OK)
            
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    @staticmethod
    def confirm_payment(request):
        url = "https://demo.vivapayments.com/api/messages/config/token"

        client_id = env('VIVA_WALLET_CLIENT_ID')
        client_secret = env('VIVA_WALLET_CLIENT_SECRET')

        credentials = "%s:%s" % (client_id, client_secret)
        encoded_credentials = base64.b64encode(bytes(credentials, 'utf-8'))
        print(encoded_credentials.decode('utf-8'))

        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': 'Basic %s' % encoded_credentials.decode('utf-8')
        }

        response = requests.get(url,
            headers=headers,
        )

        if(response.status_code==200):
            return Response(response.json(), status=status.HTTP_200_OK)
        
        return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
