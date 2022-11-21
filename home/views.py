from django.contrib.auth import authenticate,login
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from home.models import Login




def index(request):
    return render(request, 'index.html')


def loginuser(request):
    if(request.method =='POST'):
        name = request.POST.get('name')
        password= request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user is not None:
             login(request,user)
             return render(request,'users_page.html')
        else:
            return  render(request, 'login_page.html')
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