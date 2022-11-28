# Generated by Django 4.1.3 on 2022-11-28 14:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0006_remove_advertisement_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=14, region=None, verbose_name='Contact Number'),
        ),
    ]
