from django import forms

class ParkingForm(forms.Form):
    parking_id= forms.CharField(max_length=100)