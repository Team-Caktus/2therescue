from django.shortcuts import render
from .serializers import FosterSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from .models import Foster



# Create your views here.
def homepage(request):
    pets=["Graham", "Trixie", "Gigi", "Kingsley"]
    return render(request, "petrescue/homepage.html", {"pets": pets})


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

class Deletfoster(RetrieveDestroyAPIView):
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer

class NewFoster(CreateAPIView):
    serializer_class = FosterSerializer