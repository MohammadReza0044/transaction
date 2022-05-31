import imp
from tkinter import Frame
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from .models import transaction
from .serializers import transactionSerializer

class transaction_view(APIView):
    permission_classes = [IsAdminUser]

    def get (self,request):
        transactions = transaction.objects.all()
        serializer = transactionSerializer(transactions, many=True)
        return Response (serializer.data)


    def post (self,request):
        pass

