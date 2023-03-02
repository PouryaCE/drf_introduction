from rest_framework import serializers


# this serializer is for deserializing our data that come from client json => python object
class UserRegistrationSerializer(serializers.Serializer):
    username    = serializers.CharField(required=True)
    email       = serializers.EmailField(required=True)
    password1   = serializers.CharField(required=True, write_only=True)
    password2   = serializers.CharField(required=True, write_only=True)

