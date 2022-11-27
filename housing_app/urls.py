from django.urls import path
from . import views

app_name = 'housing_app'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Advertisements
    path('advertisements/', views.advertisements, name='advertisements'),
    # New Advertisement
    # path('', views.index, name='new-advertisement'),
]
