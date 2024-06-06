from django.contrib import admin
from .models import OfficeEquipment, LicenseTimer

@admin.register(OfficeEquipment)
class OfficeEquipmentAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'category', 'status', 'user', 'department', 'delivery_date')

@admin.register(LicenseTimer)
class LicenseTimerAdmin(admin.ModelAdmin):
    list_display = ('os_timer', 'antivirus_timer', 'office_timer')
    fields = ('os_timer', 'antivirus_timer', 'office_timer')
