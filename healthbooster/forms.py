from django import forms

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

class CityForm(forms.Form):
    name = forms.CharField(max_length=50)
    region = forms.CharField(max_length=50)
    population = forms.CharField(max_length=50)
    Hospital = forms.CharField(max_length=50)
    Bed = forms.CharField(max_length=50)
    Ambulance = forms.CharField(max_length=50)
