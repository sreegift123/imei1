from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth import login , logout
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from .models import *





# Create your views here.
def home(request):
    return render(request,'users/home.html',{})


def register_url(request):
    if request.method == "POST":
        fname= request.POST.get('name')

        mod=request.POST.get('model')
        mod1=request.POST.get('model1')

        imei2= request.POST.get('imei')
        imei3= request.POST.get('imei1')
        con = request.POST.get('contact')
        user=User.objects.filter(username=imei2).exists()
        if not user:
            if mod == mod1:
                user=User.objects.create_user(username=imei2,
                                              first_name=fname,
                                              email=con,
                                              password=mod,
                                              last_name=imei3)
                return render(request,'users/home.html',{})

            else:
                error = " Model Mismatch "
                return render(request,'users/home.html',{"error":error})
        else:
            return render(request,'users/home.html',{})
    else:
        return render(request,'users/home.html',{})




def check_url(request):
    if request.method == "POST":
        email_1 = request.POST.get('imei')
       
        pass_word = request.POST.get('model')
        
        user = authenticate(username=email_1,password=pass_word)
        
        if user :
            
            login(request,user)
            
            
            return render(request, 'users/check.html',{})

        else:
            error = " Sorry! IMEI NOT MATCHING "
            return render(request,'users/home.html',{"error":error})
    else:
        return render(request,'users/home.html',{})




    