from django.shortcuts import get_object_or_404, render, redirect
from .serializers import FosterSerializer, PetSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from .models import Foster, Pet, Applicant, Agency
from .forms import AdminAppForm, AppForm, PetForm, AgencyForm
# from django import forms
# from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def list_pets(request):
    pets = Pet.objects.filter((Q(status="Available") or Q(status="Adoption Pending")))
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/homepage.html", {"pets": pets, "agency": agency})


def search_by_sex_or_age_size(request):
    agency = get_object_or_404(Agency)
    query = request.GET.get('q', None)
    results = Pet.objects.filter( Q(sex__icontains=query) | Q(size__icontains=query) | Q(age_group__icontains=query))
    return render(request, "petrescue/homepage.html", {"pets": results, "agency": agency})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/pet_detail.html", {"pet": pet, "agency": agency})


def agency_detail(request):
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/about_us.html", {"agency": agency})


def AppView(request):
    agency = get_object_or_404(Agency)
    # pet = get_object_or_404(Pet, pk=pk)
    form = AppForm(data=request.POST)
    if form.is_valid():
        applicant = form.save()
        # applicant.pet_id = pet.pk
        applicant.save()
        return redirect(to="list_pets")

    return render(request, 'petrescue/application.html', {"form": form, "agency": agency})


def app_saved(request):
    agency = get_object_or_404(Agency)
    return render(request, "petrescue/app_saved.html", {"agency": agency})


@login_required
def agency(request):
    agency = get_object_or_404(Agency)
    # agency = Agency.objects.all()
    if request.method == 'GET':
        form = AgencyForm(instance=agency)
    else:
        form = AgencyForm(request.POST, request.FILES)
        if form.is_valid():
            agency = form.save()
            return redirect(to='applications')

    return render(request, "staff/agency.html", {"form": form, "agency": agency})


@login_required
def application_detail(request, pk):
    # application = Applicant.objects.get(pk=pk)
    applicant = get_object_or_404(Applicant, pk=pk)
    agency = get_object_or_404(Agency)
    if request.method == 'GET':
        form = AdminAppForm(instance=applicant)
    else:
        form = AdminAppForm(data=request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect(to='applications')

    return render(request, "staff/application_detail.html", {"form": form, "applicant": applicant, "pk": pk, "agency": agency})


@login_required
def application_list(request):
    applicants = Applicant.objects.all()
    agency = get_object_or_404(Agency)
    pets = Pet.objects.all()
    
    return render(request, "staff/application_list.html", {"applicants": applicants, "pets": pets, "agency": agency})


@login_required
def admin_pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    agency = get_object_or_404(Agency)
    # applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save()
            return redirect(to='pet_list')
    return render(request, "staff/pet_detail.html", {"form": form, "pet": pet, "pk": pk, "agency": agency})


@login_required
def add_pet(request):
    agency = get_object_or_404(Agency)
    if request.method == 'GET':
        form = PetForm()
    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save()
            pet.save()
            return redirect(to='pet_list')
    return render(request, "staff/add_pet.html", {"form": form, "agency": agency})


@login_required
def pet_list(request):
    pets = Pet.objects.all()
    applications = Applicant.objects.all()
    agency = get_object_or_404(Agency)
    return render(request, "staff/pet_list.html", {"pets": pets, "applications": applications, "agency": agency})


@login_required
def staff_home(request):
    agency = get_object_or_404(Agency)
    pets = Pet.objects.all()
    applications = Applicant.objects.all()
    return render(request, "staff/home.html", {"pets": pets, "applications": applications, "agency": agency})

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


# def login(request):
#     applicant = Applicant.objects.all()
#     return render(request, "staff/login.html", {"applicant": applicant})
#not sure what else we need here