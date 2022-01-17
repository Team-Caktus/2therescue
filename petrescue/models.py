from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
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
# 
    def __str__(self):
        return self.tag


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    # phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(max_length=150)
    foster_adopt = models.BooleanField(default=False)


class Agency(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    # phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(max_length=150)
    # logo = models.ImageField() do we use wagtail



class Pet(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=250)
    age = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    vac_status = models.BooleanField(default=False)
    # photo = image field(wagtail)
    # vet_record = models.(any wagtail solution?) as a file? or as an image? will this be its own model
    # petrescuer = this will be the foreign key to the petrescuer
    # applicant = models.ForeignKey(to="pet", on_delete=models.CASCADE, related_name="applicant")
    # agency = models.ForeignKey(to="pet", on_delete=models.CASCADE, related_name="agency")
    spay_neuter = models.BooleanField(default=False)
    # class AdoptionStatus(models.TextChoices):
    #     AVAILABLE = "av", "available"
    #     ADOPTED = "ad", "adopted"
    #     PENDING = "pd", "pending"
    # adoption_status = models.CharField(
    #     max_length=2, choices=AdoptionStatus.choices, null=True, blank=True)
    health_notes = models.TextField(max_length=500, null=True)
    tags = models.ManyToManyField(to=Tag, related_name="pets", blank=True)
    notes = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    date_updated = models.DateTimeField(default=timezone.now, null=True)


    def __str__(self):
        return self.title

#date updated vs date created how to write the "function"
#models planned
#-petrescuer(user/enduser) will have unique id
#-agency
#-admin/user(for agency) will have unique id
# need to research the class inside class for the adoptionStatus 


