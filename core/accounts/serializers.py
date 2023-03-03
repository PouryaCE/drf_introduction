from rest_framework import serializers
from django.contrib.auth.models import User

# this serializer is for deserializing our data that come from client json => python object
class UserRegistrationSerializer(serializers.Serializer):
    username    = serializers.CharField(required=True)
    email       = serializers.EmailField(required=True)
    password1   = serializers.CharField(required=True, write_only=True)
    password2   = serializers.CharField(required=True, write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("this email is already exist")
        else:
            return value


    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("this username is already exist")
        else:
            return value




    






