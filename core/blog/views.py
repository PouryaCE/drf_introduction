from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.




class PostViewSet(ViewSet):

    query_set = Post.objects.all()

    def list(self, request):
        ser_data = PostSerializer(instance = self.query_set, many=True).data
        """
            if we dont use many = True we got a terrible error
            so we must use many=True for those query that have more than one 
            objects
        """
        return Response(ser_data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        ser_data = PostSerializer(instance=self.query_set.get(pk=pk)).data
        return Response(ser_data, status=status.HTTP_200_OK)


    def create(self, request):
        ser_data = PostSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"message":"you created a post successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)



    def partial_update(self, request, pk):
        ser_data = PostSerializer(instance=self.query_set.get(pk=pk), data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        self.query_set.get(pk=pk).delete()
        return Response({"message":"you deleted this post successfully"}, status=status.HTTP_200_OK)
