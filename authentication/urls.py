from django.urls import path

from .views import user_create

urlpatterns = [
    path('signup/',user_create.as_view()),
    
]
