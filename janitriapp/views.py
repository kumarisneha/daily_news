# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from janitriapp import forms
from janitriapp.models import UserInterest, NewsWebsite
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration_page(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            interest = form.cleaned_data["interest"]
            a = UserInterest(user = user, interest=interest)
            a.save()
            form = forms.UserCreationForm()
            context = {"form": form,
            "text" : "You have succesfully registered.",}
            return render(request, 'registration.html', context )
            #return HttpResponseRedirect('/register_success/')
        else:
            context = {"form": form,}
            return render(request, 'registration.html', context)
    form = forms.UserCreationForm()
    context = {"form" : form}
    return render(request, 'registration.html', context)

def register_success(request):
    return render_to_response('register_success.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user_obj_list = User.objects.filter(email= email)
        print email
        print password
        print user_obj_list
        if len(user_obj_list) > 0:
            username = user_obj_list[0].username 
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print "Logged in"
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                context = {"text" : "Email id or password is invalid.",}
                return render(request, 'login.html', context)
        else:
            print "Email id invalid"
            return HttpResponseRedirect('/login/')
    return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def home(request):
    # user_interest=request.user.userinterest.interest
    user_interest = UserInterest.objects.get(user= request.user).interest
    filter_news= NewsWebsite.objects.filter(interest = user_interest)
    return render(request, 'home.html', {"filter_news": filter_news})

