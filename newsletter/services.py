import environ, json
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

env = environ.Env()

mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
'api_key': env('MAILCHIMP_API_KEY'),
'server': env('MAILCHIMP_REGION'),
})

class NewsletterService:
    @staticmethod
    def ping_server():
        try:
            response = mailchimp.ping.get()
            return Response(response, 
                    status=status.HTTP_200_OK)

        except ApiClientError as error:
            return Response(error.text, 
                    status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def subscribe(request):
        serializer = serializers.EmailSerializer(
                data=request.data)

        if serializer.is_valid():
            try:
                email_address = serializer.data['email']
                member_info = {
                    'email_address': email_address,
                    'status': 'subscribed',
                }

                response = mailchimp.lists.add_list_member(
                    env('MAILCHIMP_MARKETING_AUDIENCE_ID'),
                    member_info,
                )

                return Response(response, 
                        status=status.HTTP_200_OK)
            
            except ApiClientError as error:
                return Response(json.loads(error.text), 
                        status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.error_messages,
                    status=status.HTTP_400_BAD_REQUEST)
            