from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .models import OfficeEquipment, LicenseTimer

class OfficeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id_device', 'name', 'description', 'category', 'status', 'user', 'department', 'delivery_date')
    list_per_page = 25
    ordering = ('name',)

    actions = ['print_selected']

    def print_selected(self, request, queryset):
        context = {
            'objects': queryset,
            'title': 'Печать выбранных объектов',
        }
        return render(request, 'admin/print.html', context)

    print_selected.short_description = "Распечатать выбранные объекты"

admin.site.register(OfficeEquipment, OfficeEquipmentAdmin)

@admin.register(LicenseTimer)
class LicenseTimerAdmin(admin.ModelAdmin):
    list_display = ('os_timer', 'antivirus_timer', 'office_timer')
    fields = ('os_timer', 'antivirus_timer', 'office_timer')
