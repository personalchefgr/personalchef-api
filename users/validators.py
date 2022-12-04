import re

from rest_framework import serializers

class PasswordValidator:
    def __call__(self, value):
        if len(value) < 8:
            message = 'Password must contain at least 8 characters'
            raise serializers.ValidationError(message)
        
        if not re.search('.*?[A-Z]', value):
            message = 'Password must contain at least one uppercase character'
            raise serializers.ValidationError(message)

        if not re.search('.*?[a-z]', value):
            message = 'Password must contain at least one lowercase character'
            raise serializers.ValidationError(message)

        if not re.search('.*?[0-9]', value):
            message = 'Password must contain at least one numerical digit'
            raise serializers.ValidationError(message)
        
        if not re.search('.*?[#?!@$%^&*-]', value):
            message = 'Password must contain at least one special character'
            raise serializers.ValidationError(message)

        if re.search('\s', value):
            message = 'Password cannot contain whitespaces'
            raise serializers.ValidationError(message)