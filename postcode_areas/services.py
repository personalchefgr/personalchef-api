from django.shortcuts import get_object_or_404

from . import models, serializers

class PostcodeAreaService:
    @staticmethod
    def get_postcode_area_by_postcode(postcode=None):
        postcode_area = get_object_or_404(models.PostcodeArea, postcode=postcode)
        serializer = serializers.PostcodeAreaSerializer(postcode_area)

        return serializer.data