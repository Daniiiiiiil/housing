from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Advertisement
from .forms import AdvertisementForm


def index(request: HttpRequest) -> HttpResponse:
    """Homepage"""
    return render(request, 'housing_app/index.html')


def advertisements(request: HttpRequest) -> HttpResponse:
    """Renders all advertisements"""
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'housing_app/advertisements.html', context)


def advertisement(request: HttpRequest, advertisement_id: int) -> HttpResponse:
    """Renders specific advertisement by id"""
    advertisement = get_object_or_404(Advertisement, id=advertisement_id)
    context = {'advertisement': advertisement}
    return render(request, 'housing_app/advertisement.html', context)


def new_advertisement(request: HttpRequest) -> HttpResponse:
    """Renders advertisement creation form"""
    if request.method != 'POST':
        form = AdvertisementForm()
    else:
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('housing_app:advertisements'))
    context = {'form': form}
    return render(request, 'housing_app/new_advertisement.html', context)
