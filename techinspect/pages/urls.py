from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
from pages import views

urlpatterns = [
        path('', views.login_render, name='Login'),
        path('home/<str:uuid>/', views.homepage_render, name="Homepage"),
        path('signup/', views.signup_render, name="Signup"),
        path('profile/<str:uuid>/', views.profile_render, name="Profile"),
        path('waivers/<str:uuid>/', views.waiver_render, name="Waivers"),
        path('inspections/<str:uuid>/', views.inspection_render, name="Inspections"),
        path('cars/<str:uuid>/', views.cars_render, name="Your cars"),
        path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
