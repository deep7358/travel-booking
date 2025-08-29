from django import forms

class BookingForm(forms.Form):
    seats = forms.IntegerField(min_value=1)
