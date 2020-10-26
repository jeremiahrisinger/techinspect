from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render
from django.utils.html import mark_safe
from pages import forms
from pages import utils

def login_render(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            #IMPORTANT: TO ACCESS FORM DATA ALWAYS USE cleaned_data['name of field']
            try:
                if utils.login(form.cleaned_data['username'], form.cleaned_data['password']):
                    return HttpResponseRedirect('home/') 
                else:
                    messages.error(request, "Login failed due to incorrect username/password")
            except ObjectDoesNotExist:
                    messages.error(request, mark_safe("Your username isn't associated with an account. </br>Click <a href='signup/'>signup</a> to create an account."))
    else:
        form = forms.LoginForm()
    return render(request, 'login/index.html', {'form': form})


def homepage_render(request):
    return render(request, 'home/index.html')

def signup_render(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            #TODO What do we need to do about password validation?
            if form.verify_password():
                try:
                    form.create_user()
                except Exception:
                    messages.error(request, "System failed to create user; please try again.")
                else:
                    #Send user back to login page to login
                    return HttpResponseRedirect('/')
            else:
                messages.error(request, "Passwords were not equal; please try again.")
        else:
            messages.error(request, "User input was malformed or failed a test")
    else:
        form = forms.SignupForm()
    return render(request, 'signup/index.html', {'form': form})
