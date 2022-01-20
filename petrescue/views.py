from django.shortcuts import render


# Create your views here.
def homepage(request):
    pets=["Graham", "Trixie", "Gigi", "Kingsley"]
    return render(request, "petrescue/homepage.html", {"pets": pets})