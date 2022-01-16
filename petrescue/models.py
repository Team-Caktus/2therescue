from django.db import models
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
# size
# age group
# 
    def __str__(self):
        return self.tag


class Pet(models.Model):
    name = models.Charfield(max_length=50)
    breed = models.Charfield(max_length=250)
    age = models.Charfield(max_length=50)
    size = models.Charfield(max_length=50)
    description = models.TextField(max_length=500, null=True)
    vac_status = models.BooleanField(default=False)
    # photo = image field(wagtail)
    # vet_record = models.(any wagtail solution?) as a file? or as an image? will this be its own model
    # petrescuer = this will be the foreign key to the petrescuer
    adoptee = models.ForeignKey()
    agency = models.ForeignKey(to="", on_delete=models.CASCADE, related_name="")
    spay_neuter = models.BooleanField(default=False)
    class AdoptionStatus(models.TextChoices):
        AVAILABLE = "av", "available"
        ADOPTED = "ad", "adopted"
        PENDING = "pd", "pending"
    adoption_status = models.CharField(
        max_length=2, choices=AdoptionStatus.choices, null=True, blank=True)
    health_notes = models.TextField(max_length=500, null=True)
    tags = models.ManyToManyField(to=Tag, related_name="", blank=True)
    notes = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    date_updated = models.DateTimeField(default=timezone.now, null=True)


    def __str__(self):
        return self.title

#date updated vs date created how to write the "function"
#models planned
#-petresquer(user/enduser) will have unique id
#-agency
#-admin/user(for agency) will have unique id


