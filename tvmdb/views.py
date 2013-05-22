from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from mediafollower.models import UserProfile, Media, Genre
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        birth_date = request.POST.get('birthdate')
        gender = request.POST.get('gender')

        u = User.objects.create(username=username,
                                email=email,)
        u.save()
        u.set_password(password)
        up = UserProfile(user=u,
                          gender=gender,
                          birth_date=birth_date)
        u.save()
        up.save()
        return render(request, 'login.html', {'state':'Registration successful, login below', 'alert':'alert-success'})
        
    return render(request, 'register.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html', {})
