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
                    messages.error(request, mark_safe("Your username isn't associated with an account. </br>Click <a href='/signup'>signup</a> to create an account."))
    else:
        form = forms.LoginForm()
    return render(request, 'login/index.html', {'form': form})


def homepage_render(request):
    return render(request, 'home/index.html')
