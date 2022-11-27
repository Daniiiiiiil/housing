from django.shortcuts import render


def index(request):
    """Homepage"""
    return render(request, 'housing_app/index.html')
