from concurrent.futures.process import _python_exit
from ctypes import addressof
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Applicant
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class AppForm(forms.ModelForm):
        class Meta:
            model = Applicant
            fields = [
                'name',
                'phoneNumber',
                'street_line_1',
                'street_line_2',
                'city',
                'state',
                'zipcode',
                'email',
        ]


# can't seem to get phonenumberfield to work here.