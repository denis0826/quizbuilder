from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Quiz

def index(request):
    return render(request, 'index.html', {})

class LoginView(ListView):
    def get(self, request):
        return HttpResponse('result')

def my_logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect('login')