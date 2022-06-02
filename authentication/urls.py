from django.urls import path

from .views import user_create, usersList , usersList

urlpatterns = [
    path('signup/',user_create.as_view()),
    path('users/', usersList.as_view())
    
]
