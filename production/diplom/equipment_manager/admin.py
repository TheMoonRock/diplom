from django.contrib import admin
from django.urls import path
from .models import OfficeEquipment, LicenseTimer

from django.contrib import admin
from django.urls import path
from .models import OfficeEquipment

class OfficeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'status', 'user', 'department', 'delivery_date')
    list_per_page = 25
    ordering = ('name',)

    def print_view(self, request):
        obj = self.get_object(request)
        return render(request, 'admin/print.html', {'object': obj})

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('print/<int:object_id>/', self.admin_site.admin_view(self.print_view), name='print_view'),
        ]
        return my_urls + urls

admin.site.register(OfficeEquipment, OfficeEquipmentAdmin)

@admin.register(LicenseTimer)
class LicenseTimerAdmin(admin.ModelAdmin):
    list_display = ('os_timer', 'antivirus_timer', 'office_timer')
    fields = ('os_timer', 'antivirus_timer', 'office_timer')
