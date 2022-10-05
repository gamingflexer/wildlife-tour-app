from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
     #<--------- Booking related path / urls start here ------->
   path('booking-confirmation', views.booking_confirmation, name='booking_confirmation'),
]