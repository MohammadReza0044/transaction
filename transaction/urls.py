from django.urls import path

from .views import branch_1000_view , transaction_view

urlpatterns = [

   path('', transaction_view.as_view()),
   path('branch_1000/', branch_1000_view.as_view()),



]
