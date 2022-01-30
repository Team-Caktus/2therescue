
from email.policy import default
from ssl import Options
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.forms import BooleanField, IntegerField, ModelForm
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
# Create your models here.


class CustomUser(AbstractUser):
    
    def __repr__(self):
        
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


# class Tag(models.Model):
#     tag = models.CharField(max_length=100, unique=True)
# # size
# # age group
# # sex of dog
#     def __str__(self):
#         return self.tag


class Foster(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_line_1 = models.CharField(max_length=255, blank=True, null=False)
    street_line_2 = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=80, blank=True, null=False)
    state = models.CharField(max_length=80, blank=True, null=False)
    zipcode = models.IntegerField(blank=True)
    email = models.EmailField(max_length=150)
    phone = PhoneNumberField(null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    
    num_of_adults = models.IntegerField()
    # ages_of_children = models.CharField()
    any_other_pets = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name




class Applicant(models.Model):


    current_residence =(
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Condo', 'Condo'),
    )

    adopt_reason =(
        ('Companion', 'Companion'),
        ('Guard_Dog', 'Guard_Dog'),
        ('Breeding', 'Breeding'),
        ('Other', 'Other'),
    )

    status =(
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Denied', 'Denied'),
        ('Open', 'Open'),
    )

    name = models.CharField(max_length=100, blank=True, null=False)
    phone = PhoneNumberField(null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    street_line_1 = models.CharField(max_length=255, blank=True, null=False)
    street_line_2 = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=80, blank=True, null=False)
    state = models.CharField(max_length=80, blank=True, null=False)
    zipcode = models.IntegerField(blank=True)
    email = models.EmailField(max_length=150, blank=True)
    pet_id = models.ForeignKey("pet", on_delete=models.CASCADE, blank=True)
    current_residence = models.TextField(choices=current_residence, blank=True, null=False)
    primary_owner = models.CharField(max_length=150, blank=True, null=False)
    num_adults = models.IntegerField(blank=True)
    num_children = models.IntegerField(blank=True)
    ages_children = models.TextField(blank=True, null=False)
    other_pets = models.BooleanField(default=False)
    other_pets_desc = models.TextField(blank=True, null=False)
    adopt_reason = models.TextField(choices= adopt_reason, blank=True, null=False)
    vet_info = models.TextField(blank=True, null=False)
    fenced_yard = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.TextField(choices= status, default="Open")
    notes = models.TextField(blank=True, null=False)
    
    


    


    def __str__(self):
        return self.name


class Agency(models.Model):
    name = models.CharField(max_length=200)
    agency_owner = models.CharField(max_length=150, null=True)
    phone = PhoneNumberField(null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])

    street_line_1 = models.CharField(max_length=255, blank=True, null=False)
    street_line_2 = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=80, blank=True, null=False)
    state = models.CharField(max_length=80, blank=True, null=False)
    zipcode = models.IntegerField(blank=True)
    business_hours = models.TextField(blank=True, null=False)
    website_info = models.TextField(blank=True, null=False)
    description = models.TextField(max_length=250, blank=True, null=False)
    email = models.EmailField(max_length=150)
    about_us = models.TextField(blank=True, null=False)
    agency_mission = models.TextField(max_length=250, blank=True, null=False)
    facebook_url = models.URLField(max_length=250, blank=True, null=False)
    twitter_url = models.URLField(max_length=250, blank=True, null=False)
    instagram_url = models.URLField(max_length=250, blank=True, null=False)
    
    # logo = models.ImageField()

    def __str__(self):
        return self.name

class Pet(models.Model):

    options =(
        ('Available', 'Available'),
        ('Pending', 'Pending'),
        ('Adopted', 'Adopted'),
    )

    sex =(
        ('Male', 'M'),
        ('Female', 'F')
    )

    age_group = (
        ('Puppy', 'Puppy'),
        ('Young', 'Young'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
    )

    size =(
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        
    )
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=250, blank=True, null=False)
    age = models.CharField(max_length=50, blank=True, null=False)
    weight = models.CharField(max_length=50, blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    current_on_vac = models.BooleanField(default=False)
    photo = models.ImageField()
    spay_neuter = models.BooleanField(default=False)
    health_notes = models.TextField(blank=True)
    notes = models.TextField(blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=options, default='Available')
    sex = models.CharField(max_length=25, choices=sex, blank=True)
    age_group = models.CharField(max_length=15, choices=age_group, blank=True)
    size = models.CharField(max_length=15, choices=size, blank=True)
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    good_with_cats = models.BooleanField(default=False)
    heart_worm_positive = models.BooleanField(default=False)
    health_concerns = models.BooleanField(default=False)
    foster_info = models.TextField(blank=True, null=False)
    # agency = models.ForeignKey(Agency, default=None, on_delete=CASCADE, blank=True)
    



    def __str__(self):
        return self.name



#date updated vs date created how to write the "function"
#models planned
#-petrescuer(user/enduser) will have unique id
#-agency
#-admin/user(for agency) will have unique id
# need to research the class inside class for the adoptionStatus 


