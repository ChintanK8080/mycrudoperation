from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login_page.html')

def signup(request):
    return render(request, 'signup_page.html')


def users(request):
    return render(request, 'users_page.html')