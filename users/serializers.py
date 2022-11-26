from rest_framework import serializers

from . import models

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            'id', 
            'email', 
            'is_active', 
            'created_at', 
            'updated_at'
        ]


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = "__all__"


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['user']


class UserProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = "__all__"
        