from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

@login_required(login_url='/tracker/sign-in/')
def tracker_home(request):
    return render(request, 'tracker/tracker_home.html')

