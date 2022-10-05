from booking.serializers import bookingsSerializer,sanctuarySerializer,feedbackSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from booking.models import bookings,Sanctuary,Feedback
from rest_framework.response import Response
from rest_framework import status
import time

# Create your views here.

@csrf_exempt
@api_view(('POST','GET'))
def booking_confirmation(request):
    if request.method == 'POST':
        try:
            date = request.POST.get('date',time.strftime("%d/%m/%Y"))
            sanctuary = request.POST.get('sanctuary', "karnala Wildlife Sanctuary")
            slot = request.POST.get('slot', "Morning")
            #check if slot is available
            slot_avaliable = True
            booking_data = bookings.objects.filter(date=date,sanctuary=sanctuary)
            try:
                booking_data_serializer = bookingsSerializer(booking_data,many=True)
            except Exception as e:
                print(e)
                
            if len(booking_data_serializer.data)>= 6:
                slot_avaliable = False
                
            if slot_avaliable:
                data_map = {"date":date,"sanctuary":sanctuary,"slot_time":slot}
                serialized = bookingsSerializer(data=data_map)

                if serialized.is_valid():
                    serialized.save()
                return Response("Your Booking is Confirmed",status=status.HTTP_200_OK)
        except ValidationError:
            return Response("Enter Valid Date",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Slot is not available",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(('POST','GET'))
def feedback_form(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('exampleFormControlInput1',None)
            issue_type = request.POST.get('exampleFormControlInput1', "Feedback")
            client_data = request.POST.get('exampleFormControlTextarea1',None)
            issue = request.POST.get('exampleFormControlTextarea2',None)
            data_map = {"email":email,"issue_type":issue_type,"client_data":client_data,"issue":issue}
            serialized = feedbackSerializer(data=data_map)

            if serialized.is_valid():
                serialized.save()
                print(serialized.data)
            return Response("Feedback Saved",status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            Response("Data Invalid",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)
