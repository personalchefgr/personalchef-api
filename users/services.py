import environ
from time import sleep

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError

from . import models, serializers, utils

env = environ.Env()

mailchimp = MailchimpTransactional.Client(
    api_key=env('MAILCHIMP_TRANSACTIONAL_API_KEY')
)

class AuthService:
    @staticmethod
    def register_user(request):
        if request.data:
            serializer = serializers.UserRegisterSerializer(
                            data=request.data)
            
            if serializer.is_valid(raise_exception=False):
                user = serializer.create(serializer.data)

                user_subject="Καλώς ήρθες στο Personal Chef!"
                UserEmailNotificationService.send_user_email_template(
                    template_name="user_new_user_created",
                    subject=user_subject,
                    receiving_address=[{
                        "email": user.email
                    }]
                )

                admin_subject = "Νέος χρήστης - %s" % user.email
                UserEmailNotificationService.send_admin_email_template(
                    template_name="admin_new_user_created",
                    subject=admin_subject,
                )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response({"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)

        return Response({"errors": ["Missing credentials"]}, 
            status=status.HTTP_400_BAD_REQUEST)
                
    @staticmethod
    def log_in_user(request=None):
        if request.data:
            serializer = serializers.UserLoginSerializer(
                            data=request.data)

            if serializer.is_valid():
                user = authenticate(
                    request,
                    email=serializer.data['email'], 
                    password=serializer.data['password']
                )

                if user is not None:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)

                    serializer = serializers.UserSessionSerializer(
                        {
                            'id': user.id,
                            'email': user.email,
                            'accessToken': str(refresh.access_token),
                            'refreshToken': str(refresh),
                            'accessTokenExpires': "",
                        }
                    )
                    
                    return Response(
                        serializer.data, 
                        status=status.HTTP_200_OK)
                        
                return Response(
                    {"error": "Login credentials not found"},
                    status=status.HTTP_401_UNAUTHORIZED)         

            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)    
            
        return Response({"error": "Missing credentials"},
            status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def log_out_user(request):
        logout(request)

        submitted_refresh_token = request.data.get('refresh')
        
        try:
            token = RefreshToken(submitted_refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def send_password_reset_link(request):
        email = request.data.get('email')

        try:
            user = models.CustomUser.objects.get(email=email)
        except:
            user = None

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete_user():
        pass


class UserService:
    @staticmethod
    def get_logged_in_user_profile(request):
        user = request.user
        print(user)
        sleep(2)

        try:
            user_profile = models.UserProfile.objects.get(user=user)
        except:
            user_profile = models.UserProfile()

        serializer = serializers.UserProfileSerializer(user_profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def update_user_profile(request):
        user = request.user
        data = request.data
        data['user'] = user.id

        try:
            user_profile = models.UserProfile.objects.get(user=user)
            serializer = serializers.UserProfileSerializer(
                user_profile,
                data=data)
        except:
            serializer = serializers.UserProfileSerializer(
                data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK)

        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST)


class UserEmailNotificationService:
    @staticmethod
    def send_user_email_template(
        template_name, 
        template_content=[{}],
        subject="",
        receiving_address=[{}],
    ):
        message = {
            "from_email": env('EMAIL_SENDING_ADDRESS'),
            "from_name": "Personal Chef",
            "subject": subject,
            "to": receiving_address
        }

        try:
            response = mailchimp.messages.send_template(
                {
                    "template_name": template_name, 
                    "template_content": template_content, 
                    "message": message
                }
            )
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))
    
    @staticmethod
    def send_admin_email_template(
        template_name, 
        template_content=[{}],
        subject="",
    ):
        message = {
            "from_email": env('EMAIL_SENDING_ADDRESS'),
            "from_name": "Personal Chef",
            "subject": subject,
            "to": [
                {
                    "email": "info@personal-chef.gr"
                },
                {
                    "email": "a.kotsampaseris@gmail.com"
                },
            ]
        }

        try:
            response = mailchimp.messages.send_template(
                {
                    "template_name": template_name, 
                    "template_content": template_content, 
                    "message": message
                }
            )
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))