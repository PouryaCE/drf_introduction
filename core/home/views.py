# from django.shortcuts import render
# from django.views import View
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import PersonSerializer
from .models import Person
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# class Home(View):
#     def get(self, request):
#         return render(request, 'home/home_page.html')



# # my first api
# @api_view(['GET'])
# def home_page(request):
#     return Response({"name": "pourya","body":"hello from api"})



# my second api
class HomePage(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)
    """
        we must sending the serialized data, rather than the  serializer itself,
        to the response. You should change it to:
        self.data = objects.data
    """

    def post(self, request):
        name = request.query_params["name"]  # query params
        # name = request.data["name"]  with body
        return Response({"body":"hello from api", "name": name})



