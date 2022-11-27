from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Advertisement


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
    advertisement = Advertisement.objects.get(id=advertisement_id)
    context = {'advertisement': advertisement}
    return render(request, 'housing_app/advertisement.html', context)
