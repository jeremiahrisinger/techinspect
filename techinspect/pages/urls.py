from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
from pages import views

urlpatterns = [
        path('', views.login_render, name='Login'),
        path('signup/', views.signup_render, name="Signup"),
        path('profile/<str:uuid>/', views.profile_render, name="Profile"),
        path('waivers/<str:uuid>/', views.waiver_render, name="Waivers"),
        path('inspections/<str:uuid>/', views.inspection_render, name="Inspections"),
        path('add_a_car/<str:uuid>/', views.cars_render, name="Add a Car"),
        path('garage/<str:uuid>/', views.garage_render, name="Your Garage"), 
        path('manage_ti/<str:uuid>/', views.manage_ti_render, name="Add/Remove Tech Inspectors"),
        path('delete_ti/<str:uuid>/', views.manage_ti_delete),
        path('add_ti/<str:uuid>/', views.manage_ti_add),
        path('reviews/<str:uuid>/', views.review_render),
        path('get_cars/<str:uuid>/', views.review_get_cars),
        path('select_car/<str:uuid>/', views.review_get_inspection),
        path('submit_ti_insp/<str:uuid>/<str:VIN>/<int:insp_id>', views.review_set_inspection),
        path('delete_car/<str:uuid>/<str:VIN>/', views.delete_car),
        path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
