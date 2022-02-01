from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Applicant, Pet, Agency
# from phonenumber_field.modelfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class AppForm(ModelForm):
        class Meta:
            model = Applicant
            fields = [
                'name',
                'phone',
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
        ]

class AdminAppForm(ModelForm):
        class Meta:
            model = Applicant
            fields = '__all__'

class PetForm(ModelForm):
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
                'status', 
                'sex',
                'age_group',
                'size',
                'good_with_kids', 
                'good_with_dogs',
                'good_with_cats',
                'heartworm_positive',
                'health_concerns',
                'health_notes', 
                'notes', 
                'foster_info',
                ]

class AgencyForm(ModelForm):
        class Meta:
            model = Agency
            fields = [
                'name',
                'agency_owner',
                'phone',
                'street_line_1',
                'street_line_2',
                'city',
                'state',
                'zipcode',
                'email',
                'business_hours',
                'website_info',
                'description',
                'about_us',
                'agency_mission',
                'facebook_url',
                'twitter_url',
                'instagram_url',
                'logo',      
        ]