from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import transaction

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields= ['id_code', 'branch_code', 'transaction', 'created_time' ]


