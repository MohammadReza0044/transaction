from pyexpat import model
from django.db import models

class transaction(models.Model):
    branch_1000 = 'branch_1000'
    branch_1001 = 'branch_1001'
    branch_1002 = 'branch_1002'

    BRANCH_CHOICES = [
        (branch_1000, 'branch_1000'),
        (branch_1001, 'branch_1001'),
        (branch_1002, 'branch_1002'),
    ]

    id_code = models.IntegerField()
    branch_code = models.CharField(max_length=20 , choices=BRANCH_CHOICES)
    transaction= models.IntegerField()
    created_time = models.DateTimeField(auto_now= True)

