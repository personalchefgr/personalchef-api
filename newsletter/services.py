from rest_framework import status
from rest_framework.responses import Response

from . import models, serializers

class NewsletterService:
    @staticmethod
    def subscribe_email(email=None):
        pass