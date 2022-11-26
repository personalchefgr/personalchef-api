from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication, 
    BasicAuthentication, 
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_400_BAD_REQUEST, 
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

from . import services

class UserRegister(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = services.UserService.register_user(request)

        return Response(status=HTTP_200_OK)


class UserLogIn(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = services.UserService.log_in_user(request)

        if user is not None:
            return Response(user, status=HTTP_200_OK)
        
        return Response(status=HTTP_401_UNAUTHORIZED)


class UserLogOut(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        success = services.UserService.log_out_user(request)
        if success:
            return Response(status=HTTP_200_OK)
        
        return Response(status=HTTP_401_UNAUTHORIZED)
    

class UserList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = services.UserService.get_all_users()

        return Response(users, status=HTTP_200_OK)
        


class UserDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = services.UserService.get_user_by_session(request.user)
        
        if user is not None:
            return Response(user, status=HTTP_200_OK)

        return Response(status=HTTP_400_BAD_REQUEST)
