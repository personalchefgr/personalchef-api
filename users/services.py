from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from . import models, serializers

from time import sleep

class AuthService:
    @staticmethod
    def register_user(request):
        if request.data:
            serializer = serializers.UserRegisterSerializer(
                            data=request.data)
            
            if serializer.is_valid():
                user = serializer.create(serializer.data)

                return Response(status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Missing credentials."}, 
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

                    print(serializer.data)
                    
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

        return Response({"message": "Logged out successfully"},
            status=status.HTTP_200_OK)

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
