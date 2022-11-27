from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'real_estate_type',
            'location',
            'contact_number',
            'description',
            'area',
            'price',
            ]
        labels = {
            'title': 'Title',
            'real_estate_type': 'Real estate type',
            'location': 'Location',
            'contact_number': 'Contact number',
            'description': 'Description',
            'area': 'Area (sq.m.)',
            'price': 'Price (UAH)',
        }
