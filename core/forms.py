from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from core.models import Farm, Customer, Crop, OffSite, OpenHours
from users.models import User
from django.db import models
import datetime as dt

class FarmAddressForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            'name',
            'about_us',
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


HOUR_CHOICES = [(None, '------')] + [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
class HourForm(forms.ModelForm):
    class Meta:
        model = OpenHours
        exclude = ['farm']
        # fields = [
        #     'mon_start',
        #     'mon_end',
        #     'tue_start',
        #     'tue_end',
        #     'wed_start',
        #     'wed_end',
        #     'thu_start',
        #     'thu_end',
        #     'fri_start',
        #     'fri_end',
        #     'sat_start',
        #     'sat_end',
        #     'sun_start',
        #     'sun_end',
        # ]
        widgets = {
            'mon_start': forms.Select(choices=HOUR_CHOICES),
            'mon_end': forms.Select(choices=HOUR_CHOICES),
            'tue_start': forms.Select(choices=HOUR_CHOICES),
            'tue_end': forms.Select(choices=HOUR_CHOICES),
            'wed_start': forms.Select(choices=HOUR_CHOICES),
            'wed_end': forms.Select(choices=HOUR_CHOICES),
            'thu_start': forms.Select(choices=HOUR_CHOICES),
            'thu_end': forms.Select(choices=HOUR_CHOICES),
            'fri_start': forms.Select(choices=HOUR_CHOICES),
            'fri_end': forms.Select(choices=HOUR_CHOICES),
            'sat_start': forms.Select(choices=HOUR_CHOICES),
            'sat_end': forms.Select(choices=HOUR_CHOICES),
            'sun_start': forms.Select(choices=HOUR_CHOICES),
            'sun_end': forms.Select(choices=HOUR_CHOICES),
            }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'avatar',
            'bio',
            'web_link',
            'street_address',
            'street_address_line_2',
            'city',
            'state',
            'zip_code',
            'latitude',
            'longitude',
        ]

class OffSiteForm(forms.ModelForm):
    class Meta:
        model = OffSite
        fields = [
            'street_address',
            'street_address_line_2',
            'city',
            'state',
            'zip_code',
            'latitude',
            'longitude',
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
