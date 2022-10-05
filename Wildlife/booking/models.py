from django.db import models
    
class bookings(models.Model):
    date = models.DateField()
    sanctuary = models.CharField(max_length=100)
    slot = models.IntegerField(null=False,default=0)
    slot_time = models.CharField(max_length=100,default="Morning") 
    booking_time = models.DateTimeField(auto_now_add=True)
    
class Sanctuary(models.Model):
    date = models.DateField()
    slot = models.IntegerField(blank=True, null=True, default=0)