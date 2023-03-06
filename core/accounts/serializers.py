from rest_framework import serializers
from django.contrib.auth.models import User

# this serializer is for deserializing our data that come from client json => python object
# class UserRegistrationSerializer(serializers.Serializer):
#     username    = serializers.CharField(required=True)
#     email       = serializers.EmailField(required=True)
#     password1   = serializers.CharField(required=True, write_only=True)
#     password2   = serializers.CharField(required=True, write_only=True)

#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("this email is already exist")
#         else:
#             return value


#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError("this username is already exist")
#         else:
#             return value


#     def validate(self, data):
#         pass1 = data["password1"]
#         pass2 = data["password2"]
#         if pass1 and pass2 and pass1 != pass2:
#             raise serializers.ValidationError("passwords must be match")
#         else:
#             return data









# now we want to create our serializer with model serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")
        extra_kwargs = {
            "password":{"required":True, "write_only":True},
            "username":{"required":True, "validators":[]},
            "email":{"required":True}
        }


    def create(self, validated_data):
        del validated_data["password2"]
        User.objects.create_user(**validated_data)


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("این ایمیل وجود دارد")
        else:
            return value


    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("این نام کاربری وجود دارد")
        else:
            return value


    def validate(self, data):
        pass1 = data["password"]
        pass2 = data["password2"]
        print(pass1)
        print(pass2)
        if pass1 and pass2 and pass1 != pass2:
            raise serializers.ValidationError("رمز عبور ها باید یکسان باشند")
        else:
            return data






