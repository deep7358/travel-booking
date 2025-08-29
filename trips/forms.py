from django import forms

class TripFilterForm(forms.Form):
    type = forms.ChoiceField(choices=[('', 'Any'), ('Flight', 'Flight'), ('Train', 'Train'), ('Bus', 'Bus')], required=False)
    source = forms.CharField(required=False)
    destination = forms.CharField(required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
