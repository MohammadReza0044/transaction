from dataclasses import fields
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from .models import user

class userSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    branch_code = serializers.CharField()
    password = serializers.CharField()


    class Meta:
        model = user
        fields = ['username', 'email', 'branch_code', 'password']

    def validate(self, attrs):
        username_exist = user.objects.filter(username=attrs['username']).exists()

        if username_exist:
            raise serializers.ValidationError(detail="this user is exits")

        email_exist = user.objects.filter(username=attrs['email']).exists()

        if email_exist:
            raise serializers.ValidationError(detail="this email is exits")

        return super().validate(attrs)

    
