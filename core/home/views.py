# from django.shortcuts import render
# from django.views import View
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 
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
    def get(self, request):
        return Response({"name": "pourya","body":"hello from api"})
        