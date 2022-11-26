from . import serializers

class ContactFormService:
    @staticmethod
    def create_new_message(request):
        serializer = serializers.MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return True, serializer.data
        
        return False, serializer.errors