from cgitb import reset
import imp
import stat
from sys import api_version
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from .models import user
from .serializers import userSerializer


class user_create(APIView):
    def post (self,request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response (serializer.errors , status= status.HTTP_400_BAD_REQUEST)
        

class usersList(APIView):
    def get (self,request):
        users=user.objects.all()
        serializer = userSerializer(users , many=True)
        return Response (serializer.data)

