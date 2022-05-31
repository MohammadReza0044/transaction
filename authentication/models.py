from django.db import models

from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class customUserManager(BaseUserManager):

    def user_create (self, email, password, **extra_fields):
        if not email:
            raise ValueError (_("you must enter an email"))
        email=self.normalize_email(email)
        new_user = self.model (email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user


    def create_seperUser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.setdefault('is_staff') is not True:
            raise ValueError (_('supperuser must have is_staff as True'))
        
        if extra_fields.setdefault('is_superuser') is not True:
            raise ValueError (_('supperuser must have is_superuser as True'))

        if extra_fields.setdefault('is_active') is not True:
            raise ValueError (_('supperuser must have is_active as True'))

        return self.create_user(email,password,**extra_fields)



class user (AbstractUser):

    branch_1000 = 'branch_1000'
    branch_1001 = 'branch_1001'
    branch_1002 = 'branch_1002'

    BRANCH_CHOICES = [
        (branch_1000, 'branch_1000'),
        (branch_1001, 'branch_1001'),
        (branch_1002, 'branch_1002'),
    ]
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    branch_code = models.CharField(max_length=50, choices=BRANCH_CHOICES, default= branch_1000)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'branch_code']

    def __str__(self):
        return f"<user {self.email}"




