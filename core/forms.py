from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from core.models import Farm, Customer, Crop
from users.models import User
from django.db import models

class FarmForm(forms.ModelForm):
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
        ]

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [
            'item'
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
            'farm',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user

        # widgets = {
        # 'username' : forms.TextInput(attrs={'class':'form-control'}),
        # 'email' : forms.TextInput(attrs={'class':'form-control'}),            
    # }

# class CustomerRegistrationFrom(UserCreationForm):

#     required_css_class = 'required'
