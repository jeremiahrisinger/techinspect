from django.urls import path

from pages import views

urlpatterns = [
        path('', views.login_render, name='Login'),
        path('home/', views.homepage_render, name="Homepage"),
]

