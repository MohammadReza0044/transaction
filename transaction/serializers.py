from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import transaction

class transactionSerializer(serializers.ModelSerializer):

    id_code = serializers.IntegerField()
    branch_code = serializers.CharField()
    transaction= serializers.IntegerField()
    created_time = serializers.DateTimeField()

    class Meta:
        model = transaction
        fields= ['id_code', 'branch_code', 'transaction', 'created_time' ]


