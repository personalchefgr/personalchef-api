from rest_framework.serializers import ModelSerializer

from . import models

class MessageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        exclude = ['created_at']