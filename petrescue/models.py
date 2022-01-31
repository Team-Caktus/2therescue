from django.db import models
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# from modelcluster.fields import ParentalKey
# from wagtail.core.models import Page, Orderable
# from wagtail.core.fields import RichTextField
# from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
# from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.search import index

class CustomUser(AbstractUser):
    
    def __repr__(self):
        
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Foster(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=False)
    street_line_1 = models.CharField(max_length=255, blank=True, null=False)
    street_line_2 = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=80, blank=True, null=False)
    state = models.CharField(max_length=80, blank=True, null=False)
    zipcode = models.CharField(max_length=5, blank=True)
    email = models.EmailField(max_length=150, blank=True, null=False)
    phoneRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneRegex], max_length = 16, blank=True, null=False)
    num_of_adults = models.CharField(max_length=50, blank=True, null=False)
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

    name = models.CharField("full name", max_length=100, blank=True, null=False)
    phoneRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField("primary phone", validators = [phoneRegex], max_length=16, blank=True, null=False)
    street_line_1 = models.CharField("street address", max_length=255, blank=True, null=False)
    street_line_2 = models.CharField("street address line 2",max_length=255, blank=True, null=False)
    city = models.CharField(max_length=80, blank=True, null=False)
    state = models.CharField(max_length=80, blank=True, null=False)
    zipcode = models.CharField(max_length=5, blank=True)
    email = models.EmailField(max_length=150, blank=True, null=False)
    pet_id = models.ForeignKey('Pet', verbose_name="name of pet you're applying for", on_delete=models.CASCADE)
    current_residence = models.TextField("type of home", choices=current_residence, blank=True, null=False)
    primary_owner = models.CharField("full name of intended primary owner", max_length=150, blank=True, null=False)
    num_adults = models.CharField("number of adults in the home", max_length=50, blank=True, null=False)
    num_children = models.CharField("number of children in the home", max_length=50, blank=True, null=False)
    ages_children = models.TextField("ages of children in the home", blank=True, null=False)
    other_pets = models.BooleanField("do you currently have any other pets?", default=False)
    other_pets_desc = models.TextField("if yes, please list them below", blank=True, null=False)
    adopt_reason = models.TextField("reason you're interested in adopting a pet", choices=adopt_reason, blank=True, null=False)
    vet_info = models.TextField(blank=True, null=False)
    fenced_yard = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=status, default="Open")
    notes = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

class Agency(models.Model):
    name = models.CharField("rescue organization",max_length=200, blank=True, null=False)
    agency_owner = models.CharField("rescue owner", max_length=150, blank=True, null=False)
    phoneRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField("phone number", validators = [phoneRegex], max_length=16, blank=True, null=False)
    street_line_1 = models.CharField("street address", max_length=255, blank=True, null=False)
    street_line_2 = models.CharField("street address line 2", max_length=255, blank=True, null=False)
    city = models.CharField(max_length=80, blank=True, null=False)
    state = models.CharField(max_length=80, blank=True, null=False)
    zipcode = models.CharField(max_length=5, blank=True)
    business_hours = models.TextField(blank=True, null=False)
    website_info = models.TextField(blank=True, null=False)
    description = models.TextField(max_length=250, blank=True, null=False)
    email = models.EmailField(max_length=150, blank=True, null=False)
    about_us = models.TextField(blank=True, null=False)
    agency_mission = models.TextField(max_length=250, blank=True, null=False)
    facebook_url = models.URLField(max_length=250, blank=True, null=False)
    twitter_url = models.URLField(max_length=250, blank=True, null=False)
    instagram_url = models.URLField(max_length=250, blank=True, null=False)
    logo = models.ImageField(blank=True)

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

    name = models.CharField(max_length=50, blank=True, null=False)
    breed = models.CharField(max_length=250, blank=True, null=False)
    age = models.CharField(max_length=50, blank=True, null=False)
    weight = models.CharField(max_length=50, blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    current_on_vac = models.BooleanField("up-to-date vaccinations ", default=False)
    photo = models.ImageField(blank=True)
    spay_neuter = models.BooleanField(default=False)
    health_notes = models.TextField(blank=True)
    notes = models.TextField(blank=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=options, default='Available')
    sex = models.CharField(max_length=25, choices=sex, blank=True)
    age_group = models.CharField(max_length=15, choices=age_group, blank=True)
    size = models.CharField(max_length=15, choices=size, blank=True)
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    good_with_cats = models.BooleanField(default=False)
    heartworm_positive = models.BooleanField(default=False)
    health_concerns = models.BooleanField("other health concerns", default=False)
    foster_info = models.TextField(blank=True, null=False)
    # agency = models.ForeignKey(Agency, default=None, on_delete=CASCADE, blank=True)

    def __str__(self):
        return self.name

# class Tag(models.Model):
#     tag = models.CharField(max_length=100, unique=True)
# # size
# # age group
# # sex of dog
#     def __str__(self):
#         return self.tag