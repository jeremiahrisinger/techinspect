from django.contrib import admin

# Register your models here.
from pages.models import *

class VehicleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vehicle, VehicleAdmin)

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(TIUser, UserAdmin)

class WaiverAdmin(admin.ModelAdmin):
    pass

admin.site.register(Waiver, WaiverAdmin)

class InspectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inspection, InspectionAdmin)
