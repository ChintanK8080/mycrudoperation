from django.http import HttpResponse
from django.shortcuts import render
from home.models import Login


def index(request):
    return render(request, 'index.html')


def login(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        login = Login(name=name,address=address,age=age,phone=phone)
        login.save()
    return render(request, 'login_page.html')

def signup(request):
    return render(request, 'signup_page.html')


def users(request):
    return render(request, 'users_page.html')