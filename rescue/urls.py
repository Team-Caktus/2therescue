"""rescue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from petrescue import views as petrescue_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('', petrescue_views.homepage, name='home'),
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    path('foster/<int:pk>/', petrescue_views.FosterDetail.as_view(), name='Foster_detail'),
    path('foster/new/', petrescue_views.AddFoster.as_view(), name='add_Foster'),
    path('foster/Foster_list/', petrescue_views.FosterList.as_view(), name='Foster_list'),
    path('foster/edit/<int:pk>/', petrescue_views.EditFoster.as_view(), name='edit_Foster'),
    path('foster/Foster_detail/<int:pk>/', petrescue_views.FosterDetail.as_view(), name='Foster_detail'),
    path('foster/delete_Foster/<int:pk>', petrescue_views.Deletefoster.as_view(), name='delete_Foster'),
    path('foster/create/',petrescue_views.NewFoster.as_view(), name="create_Foster"),
    path('pet/<int:pk>/', petrescue_views.PetDetail.as_view(), name='pet_detail'),
    path('pet/new/', petrescue_views.NewPet.as_view(), name='add_pet'),
    path('pet/pet_list/', petrescue_views.PetList.as_view(), name='pet_list'),
    path('pet/edit/<int:pk>/', petrescue_views.EditPet.as_view(), name='edit_pet'),
    path('pet/delete_pet/<int:pk>', petrescue_views.DeletePet.as_view(), name='delete_pet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    