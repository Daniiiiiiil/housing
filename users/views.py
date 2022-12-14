from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """LogOut from web-application"""
    logout(request)
    return HttpResponseRedirect(reverse('housing_app:index'))


def register(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """Register a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1']
                                              )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('housing_app:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
