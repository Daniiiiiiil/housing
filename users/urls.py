from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # LogOut page
    path('logout/', views.logout_view, name='logout'),
    # LogIn page
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'
         ),
    # Registration page
    path('register/', views.register, name='register'),
]
