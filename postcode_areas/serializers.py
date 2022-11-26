from rest_framework.serializers import ModelSerializer

from . import models

class PostcodeAreaSerializer(ModelSerializer):
    class Meta:
        model = models.PostcodeArea
        fields = "__all__"
