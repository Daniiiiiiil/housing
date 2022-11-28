from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Advertisement(models.Model):
    """Advertisement for the sale of real estate"""
    # Real estate type options
    REAL_ESTATE_TYPE = (
        ('room', 'Room'),
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('storage', 'Storage'),
        ('garage', 'Garage'),
        ('commercial', 'Commercial'),
    )

    title = models.CharField("Advertisement Title", max_length=50)
    real_estate_type = models.CharField(
        "Real Estate Type",
        max_length=10,
        choices=REAL_ESTATE_TYPE
        )
    location = models.CharField("Location", max_length=50, default="Kyiv")
    contact_number = PhoneNumberField(
        "Contact Number",
        max_length=14,
        blank=False
        )
    description = models.TextField("Description", max_length=250, blank=True)
    area = models.FloatField("Area (sq.m.)", default=1.0)
    price = models.FloatField("Price (UAH)", default=0)

    def __str__(self):
        """Returns the string representation of the model"""
        return self.title
