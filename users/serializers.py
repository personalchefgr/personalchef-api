from rest_framework import serializers
from django.db import IntegrityError

from rest_framework.validators import UniqueValidator

from . import models, validators

class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=models.CustomUser.objects.all()
            )
        ]
    )
    
    password = serializers.CharField(
        max_length=200,
        validators=[
            validators.PasswordValidator()
        ]
    )

    confirm_password = serializers.CharField(max_length=200)

    def validate(self, data):
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        if (password != confirm_password):
            raise serializers.ValidationError("Passwords do not match")

        return data


    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        
        user = models.CustomUser.objects.create_user(
            email=email, 
            password=password)
        
        return user
        

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)


class UserSessionSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    accessToken = serializers.CharField(max_length=250)
    refreshToken = serializers.CharField(max_length=250)
    accessTokenExpires = serializers.CharField(max_length=250)


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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'