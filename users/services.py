from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from . import models, serializers

class UserService:
    @staticmethod
    def register_user(request):
        pass

    @staticmethod
    def log_in_user(request=None):
        if request.data:
            serializer = serializers.UserLoginSerializer(data=request.data)

            if serializer.is_valid():
                user = authenticate(
                    request,
                    email=serializer.data['email'], 
                    password=serializer.data['password']
                )

                if user is not None:
                    login(request, user)
                    serializer = serializers.UserDetailsSerializer(user)
                    
                    return Response(serializer.data, status=status.HTTP_200_OK)
                    
        return Response(status=status.HTTP_401_UNAUTHORIZED)

        

    @staticmethod
    def log_out_user(request):
        submitted_refresh_token = request.data.get('refresh')
        
        try:
            token = RefreshToken(submitted_refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def delete_user():
        pass

    @staticmethod
    def get_all_users():
        users = models.CustomUser.objects.all()
        serializer = serializers.UserListSerializer(users, many=True)

        return serializer.data

    @staticmethod
    def get_user_by_session(request):
        serializer = serializers.UserDetailsSerializer(requ)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        

    @staticmethod
    def get_user_by_id(id=None):
        user = get_object_or_404(models.CustomUser, id=id)
        serializer = serializers.UserDetailsSerializer(user)

        return serializer.data

    @staticmethod
    def get_user_profile_by_user():
        pass