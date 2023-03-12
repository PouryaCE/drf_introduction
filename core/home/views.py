# from django.shortcuts import render
# from django.views import View
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import PersonSerializer, AnswerSerializer, QuestionSerializer
from .models import Person, Answer, Question
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework import status
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





class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True).data
        return Response(data=ser_data)


    def post(self, request):
        ser_data = QuestionSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"message":"your question sent successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"message":"you updated this question successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        question = Question.objects.get(pk=pk).delete()
        return Response({"message":"deleted successfully"})