from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.


class UserRegistraion(APIView):
    def post(self, request):
        ser_data = UserRegistrationSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors)