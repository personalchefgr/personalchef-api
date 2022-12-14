import environ, requests, base64

from rest_framework import status
from rest_framework.response import Response

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
    def create_payment_order(request, _access_token=None):
        if _access_token is not None:
            base_url = env('VIVA_WALLET_API_URL')
            url = base_url + 'checkout/v2/orders'

            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer %s' % _access_token
            }

            payload = {
                "amount": int(3000),
                "sourceCode": str(6530) #env('VIVA_WALLET_PAYMENT_SOURCE_CODE')
            }
            
            response = requests.post(url,
                headers=headers,
                data=payload,
            )
            print(response.json())

            if(response.status_code==200):
                print(response.json())
                return Response(response.json(), status=status.HTTP_200_OK)
            
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'Authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)
        