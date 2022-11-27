from django.urls import path
from . import views

app_name = 'housing_app'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # All advertisements page
    path('advertisements/', views.advertisements, name='advertisements'),
    # Specific advertisement page
    path('advertisement/<int:advertisement_id>',
         views.advertisement,
         name='advertisement'
         ),
    # New advertisement creation page
    path('new_advertisement/',
         views.new_advertisement,
         name='new_advertisement'
         ),
]
