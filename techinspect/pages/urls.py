from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from pages import views

urlpatterns = [
        path('', views.login_render, name='Login'),
        path('home/', views.homepage_render, name="Homepage"),
        path('signup/', views.signup_render, name="Signup")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
