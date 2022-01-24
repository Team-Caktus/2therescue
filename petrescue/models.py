
from ssl import Options
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


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


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
# size
# age group
# sex of dog
    def __str__(self):
        return self.tag


class Foster(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_line_1 = models.CharField(max_length=255, blank=False, null=True)
    street_line_2 = models.CharField(max_length=255, blank=False, null=True)
    city = models.CharField(max_length=80, blank=False, null=True)
    state = models.CharField(max_length=80, blank=False, null=True)
    zipcode = models.IntegerField(default=False)
    email = models.EmailField(max_length=150)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    num_of_adults = models.IntegerField()
    ages_of_children = models.CharField(max_length=50)
    any_other_pets = models.BooleanField(default=False)

    def __str__(self):
        return self.foster




class Applicant(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    street_line_1 = models.CharField(max_length=255, blank=False, null=True)
    street_line_2 = models.CharField(max_length=255, blank=False, null=True)
    city = models.CharField(max_length=80, blank=False, null=True)
    state = models.CharField(max_length=80, blank=False, null=True)
    zipcode = models.IntegerField(default=False)
    email = models.EmailField(max_length=150)
    foster_adopt = models.BooleanField(default=False)

    def __str__(self):
        return self.applicant


class Agency(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    street_line_1 = models.CharField(max_length=255, blank=False, null=True)
    street_line_2 = models.CharField(max_length=255, blank=False, null=True)
    city = models.CharField(max_length=80, blank=False, null=True)
    state = models.CharField(max_length=80, blank=False, null=True)
    zipcode = models.IntegerField(default=False)
    email = models.EmailField(max_length=150)
    # logo = models.ImageField()

    def __str__(self):
        return self.agency

class Pet(models.Model):

    options =(
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('adopted', 'Adopted'),
    )
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=250)
    age = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    vac_status = models.BooleanField(default=False)
    image_url = models.CharField(max_length=250, blank=True, null=True)
    spay_neuter = models.BooleanField(default=False)
    health_notes = models.TextField(max_length=500, null=True)
    tags = models.ManyToManyField(to=Tag, related_name="pets", blank=True)
    notes = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    date_updated = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=25, choices=options, default='available')


    def __str__(self):
        return self.title



#date updated vs date created how to write the "function"
#models planned
#-petrescuer(user/enduser) will have unique id
#-agency
#-admin/user(for agency) will have unique id
# need to research the class inside class for the adoptionStatus 


