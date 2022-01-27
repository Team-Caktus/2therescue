from django.shortcuts import get_object_or_404, render, redirect
from .serializers import FosterSerializer, PetSerializer, AgencySerializer, ApplicantSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from .models import Foster, Pet, Applicant, Agency
from .forms import AppForm
from django import forms


class FosterList(generics.ListCreateAPIView):
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer

class FosterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer

class AddFoster(CreateAPIView):
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer

class EditFoster(RetrieveUpdateDestroyAPIView):
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer

class Deletefoster(RetrieveDestroyAPIView):
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer

def list_pets(request):
    pets = Pet.objects.all()
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/homepage.html", {"pets": pets, "agency": agency})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/pet_detail.html", {"pet": pet, "agency": agency})

def agency_detail(request):
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/contact_us.html", {"agency": agency})

class NewFoster(CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class EditPet(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class DeletePet(RetrieveDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class NewPet(CreateAPIView):
    serializer_class = PetSerializer
   
def AppView(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    form = AppForm(data=request.POST)
    if form.is_valid():
        applicant = form.save()
        applicant.pet_id = pet.pk
        applicant.save()
        return redirect(to="application_submitted")

    return render(request, 'petrescue/application.html', {'form': form, 'pet':pet, 'pk':pk})