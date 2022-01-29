from concurrent.futures.process import _python_exit
from ctypes import addressof
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Applicant, Pet
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
                'pet_id',
                'current_residence',
                'primary_owner',
                'num_adults',
                'num_children',
                'ages_children',
                'other_pets',
                'other_pets_desc',
                'adopt_reason', 
                'vet_info',
                'fenced_yard',
                'date_created',
                'date_updated',   
        ]


class PetForm(forms.ModelForm):
        class Meta:
            model = Pet
            fields = [
                'name',
                'breed',
                'age',
                'weight',
                'description',
                'current_on_vac',
                'photo',
                'spay_neuter',
                'health_notes', 
                'tags', 
                'notes', 
                'date_created',
                'date_updated',
                'status', 
                'sex',
                'age_group',
                'size',
                'good_with_kids', 
                'good_with_dogs',
                'good_with_cats',
                'heart_worm_positive',
                ]



# can't seem to get phonenumberfield to work here.