from django.urls import path
from . import views

app_name = 'housing_app'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
]
