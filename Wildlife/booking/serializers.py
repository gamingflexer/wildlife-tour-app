from rest_framework import serializers
from booking.models import *


class bookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookings
        fields = "__all__"
        
class sanctuarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanctuary
        fields = "__all__"
        
class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"