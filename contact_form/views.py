from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .services import ContactFormService

class MessageDetails(APIView):
    def post(self, request):
        success, response = ContactFormService.create_new_message(request)

        if success:
            return Response(response, status=HTTP_201_CREATED)

        return Response(response, status=HTTP_400_BAD_REQUEST)
