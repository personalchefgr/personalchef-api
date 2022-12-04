from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_400_BAD_REQUEST, 
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

from .services import AuthService, UserService


class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = UserService.get_all_users()

        return Response(users, status=HTTP_200_OK)
        

class UserDetails(APIView):
    permission_classes = []

    def get(self, request):
        response = UserService.get_logged_in_user(request)

        return response


class UserProfile(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        response = UserService.get_logged_in_user_profile(request)

        return response

    def post(self, request):
        response = UserService.update_user_profile(request)

        return response

class UserRegister(APIView):
    permission_classes = []

    def post(self, request):
        response = AuthService.register_user(request)

        return response


class UserLogIn(APIView):
    permission_classes = []

    def post(self, request):
        response = AuthService.log_in_user(request)
        
        return response

class UserLogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = AuthService.log_out_user(request)
        
        return response
