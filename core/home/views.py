# from django.shortcuts import render
# from django.views import View
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import PersonSerializer, QuestionSerializer, UserSerializer
from .models import Person, Question
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from permissions import IsSuperUser, IsSuperUserORStaffReadOnly, IsSuperUserOrOwner
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




class UserShowView(APIView):
    permission_classes = [IsAuthenticated, IsSuperUserORStaffReadOnly]

    def get(self, request):
        users = User.objects.all()
        self.check_object_permissions(self.request, users)
        ser_data = UserSerializer(instance=users, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)




class UserUpdateView(APIView):
    permission_classes = [IsSuperUserOrOwner,IsAuthenticated]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        self.check_object_permissions(request, user)
        ser_data = UserSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"message":"you updated this user successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreationView(APIView):
    permission_classes = [IsSuperUser,IsAuthenticated]


    def post(self, request):
        self.check_object_permissions(request, None)
        ser_data = UserSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"message":"you created a user successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDeleteView(APIView):
    permission_classes = [IsSuperUserOrOwner,IsAuthenticated]


    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response({"message":"you deleted user successfully"}, status=status.HTTP_200_OK)