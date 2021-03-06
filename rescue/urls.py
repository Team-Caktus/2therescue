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
# from unicodedata import name
from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from petrescue import views as petrescue_views

# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail.core import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path("", petrescue_views.list_pets, name="list_pets"),
    path("manage/", petrescue_views.staff_home, name="home"),
    path("pets/<int:pk>/", petrescue_views.pet_detail, name="get_pet"),
    path("about_us/", petrescue_views.agency_detail, name="agency_detail"),
    path('agency/', petrescue_views.agency, name='agency'),
    path('application/<int:pk>/', petrescue_views.application_detail, name='application_detail'),
    path('applications/', petrescue_views.application_list, name='applications'),
    # path('login/', petrescue_views.login, name='login'),
    path('pet_detail/<int:pk>/', petrescue_views.admin_pet_detail, name='admin_pet_detail'),
    path('add_pet/', petrescue_views.add_pet, name='add_pet'),
    path('pet_list/', petrescue_views.pet_list, name='pet_list'),
    # path('cms/', include(wagtailadmin_urls)),
    # path('documents/', include(wagtaildocs_urls)),
    path('application/', petrescue_views.AppView, name='application'),
    path('success/', petrescue_views.app_saved, name='app_saved'),
    path('search', petrescue_views.search_by_sex_or_age_size, name='search_by_sex_or_age_size'),
    path('add_pet', petrescue_views.add_pet, name="add_pet")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)