from tokenize import group
from django.contrib.auth.models import Group, Permission

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAdminUser , IsAuthenticated

from .models import transaction
from .serializers import transactionSerializer
from authentication.models import user

class transaction_view(APIView):
    permission_classes = [IsAdminUser]

    def get (self,request):
        transactions = transaction.objects.all()
        serializer = transactionSerializer(transactions, many=True)
        return Response (serializer.data)


    def post (self,request):
        pass


class branch_1000_view(APIView):
    
    
    def get(self,request):
         transactions = transaction.objects.filter ( branch_code = 'branch_1000')
         serializer = transactionSerializer(transactions, many=True)
         return Response (serializer.data)
