from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

from pages import forms
from pages import utils

def login_render(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            #IMPORTANT: TO ACCESS FORM DATA ALWAYS USE cleaned_data['name of field']
            if utils.login(form.cleaned_data['username'], form.cleaned_data['password']):
                print("Getting here!!!")
                return HttpResponseRedirect('home/') 
    else:
        form = forms.LoginForm()
    return render(request, 'login/index.html', {'form': form})


def homepage_render(request):
    return render(request, 'home/index.html')
