from django.http import HttpResponse, Http404

from django.shortcuts import render

def login_render(request):
    return render(request, 'login/index.html')
def homepage_render(request):
    return render(request, 'home/index.html')
