from django.contrib import admin
from .models import OfficeEquipment, LicenseTimer

@admin.register(OfficeEquipment)
class OfficeEquipmentAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'category', 'status', 'user', 'department', 'delivery_date')

