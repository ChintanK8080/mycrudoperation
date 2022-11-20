from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from home.models import Login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login_page.html')




def signup(request):
    if(request.method == 'POST'):
       name = request.POST.get('name')
       address = request.POST.get('address')
       phone = request.POST.get('phone')
       age = request.POST.get('age')
       login = Login(name=name,address=address,age=age,phone=phone)
       login.save()
       messages.success(request,"profile updated successfully")
       return redirect('/login') 
    return render(request, 'signup_page.html')


def users(request):
    return render(request, 'users_page.html')