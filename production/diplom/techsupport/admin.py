from django.contrib import admin

# Register your models here.

from .models import Problems #Employee
class ProblemsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', 'id_request', 'nemployee', 'request_from_date', 'name_of_problem', 'description_of_problem')
        }),
        ('Статус заявки', {
            'fields': ('status', 'date_of_finish'),
            'classes': ('collapse',),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['status', 'date_of_finish']
        return []

admin.site.register(Problems, ProblemsAdmin)
