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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from petrescue import views as petrescue_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

router = DefaultRouter(trailing_slash=False)
router.register("agency", petrescue_views.AgencyViewSet, basename="agency")
router.register("applicant", petrescue_views.ApplicantViewSet, basename="applicant")


urlpatterns = [
    path("api/", include(router.urls)),
    path('', petrescue_views.homepage, name='home'),
    path("", petrescue_views.list_pets, name="list_pets"),
    path("pets/<int:pk>/", petrescue_views.pet_detail, name="get_pet"),
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    path('application/', petrescue_views.AppView, name='application')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
