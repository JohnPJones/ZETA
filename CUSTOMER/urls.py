from django.urls import path 
from .views import CustomerInput,Customer
urlpatterns = [
    
    path('',Customer,name = 'Customer'),
    path('createcustomer/',CustomerInput,name = 'CreateCustomer')

]