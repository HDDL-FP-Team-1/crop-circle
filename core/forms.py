from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from core.models import Farm, Customer, Crop
from users.models import User
from django.db import models

class FarmAddressForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            'name',
            'website',
            'street_address',
            'street_address_line_2',
            'city',
            'state',
            'zip_code',
            'image',
            'latitude',
            'longitude',
        ]
        widgets = {'latitude': forms.HiddenInput(), 'longitude': forms.HiddenInput()}
        

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [
            'item'
        ]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'avatar',
        ]

class FarmRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(max_length=55)

    class Meta:
        model= User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
