from django.shortcuts import get_object_or_404, render
from .serializers import FosterSerializer, PetSerializer, AgencySerializer, ApplicantSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from .models import Foster, Pet, Applicant, Agency
# from rest_framework import viewsets

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
    return render(request, "petrescue/homepage.html", {"pets": pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, "petrescue/pet_detail.html", {"pet": pet, "pk":pk})

def agency_detail(request, pk):
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


# class ApplicantViewSet(ModelViewSet):
#     queryset = Applicant.objects.all()
#     serializer_class = ApplicantSerializer
#     permission_classes = []

#     def get_serializer_class(self):
#         if self.action in ["list"]:
#           return ApplicantSerializer
#         return super().get_serializer_class()





