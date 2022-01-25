from django.shortcuts import get_object_or_404, render
from .serializers import FosterSerializer, PetSerializer, AgencySerializer, ApplicantSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from .models import Foster, Pet, Applicant, Agency
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet



# Create your views here.

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
    serializer_class = FosterSerializer

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def list_pets(request):
        pets = Pet.objects.all()
        return render(request, "petrescue/homepage.html", {"pets": pets})


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_pet(request, pk):
        pet = get_object_or_404(Pet,pk=pk)
        return render(request, "petrescue/pet_detail.html", {"pet": pet})


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


class ApplicantViewSet(ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ["list"]:
          return ApplicantSerializer
        return super().get_serializer_class()


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ["list"]:
           return AgencySerializer
        return super().get_serializer_class()






