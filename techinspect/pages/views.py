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
                    return HttpResponseRedirect('home/' + utils.user_list[form.cleaned_data['username']].uuid + '/') 
                else:
                    messages.error(request, "Login failed due to incorrect username/password")
            except ObjectDoesNotExist:
                    messages.error(request, mark_safe("Your username isn't associated with an account. </br>Click <a href='signup/'>here</a> to create an account."))
    else:
        form = forms.LoginForm()
    return render(request, 'login/index.html', {'form': form})


def homepage_render(request, uuid):
    print(uuid)
    return render(request, 'home/index.html', {'uuid': uuid})

def profile_render(request, uuid):
    return render(request, 'profile/profile.html', {'uuid': uuid})

def inspection_render(request, uuid):
    return render(request, 'inspections/inspections.html', {'uuid': uuid})

def schedule_render(request, uuid):
    return render(request, 'schedule/schedule.html', {'uuid': uuid})
def waiver_render(request, uuid):
    if request.method == 'POST':
        form = forms.WaiverForm(request.POST)
        if form.is_valid():
            pass
                #Add the waiver into the database for the given person.
    else:
        form = forms.WaiverForm()
    return render(request, 'waivers/waivers.html', {'waiver_form': form, 'uuid': uuid})


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

    
