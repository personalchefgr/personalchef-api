from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout

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
                    return serializer.data

            print(serializer.errors)
        return None

        

    @staticmethod
    def log_out_user(request):
        if request.user.is_authenticated:
            logout(request)
            return True
        
        return False

    @staticmethod
    def delete_user():
        pass

    @staticmethod
    def get_all_users():
        users = models.CustomUser.objects.all()
        serializer = serializers.UserListSerializer(users, many=True)

        return serializer.data

    @staticmethod
    def get_user_by_session(current_user=None):
        if current_user.is_authenticated:
            serializer = serializers.UserDetailsSerializer(current_user)
            
            return serializer.data
        
        return None

    @staticmethod
    def get_user_by_id(id=None):
        user = get_object_or_404(models.CustomUser, id=id)
        serializer = serializers.UserDetailsSerializer(user)

        return serializer.data

    @staticmethod
    def get_user_profile_by_user():
        pass