from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Problems

class ProblemsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', 'request_from_date', 'name_of_problem', 'description_of_problem')
        }),
        ('Статус заявки', {
            'fields': ('status', 'date_of_finish'),
            'classes': ('collapse',),
        }),
    )

    list_display = ('user', 'request_from_date', 'name_of_problem', 'status', 'date_of_finish')
    list_per_page = 25
    ordering = ('request_from_date',)

    actions = ['print_selected']

    def print_view(self, request, object_id):
        obj = self.get_object(request, object_id)
        return render(request, 'admin/print.html', {'object': obj})

    def print_selected(self, request, queryset):
        return render(request, 'admin/print_selected.html', {'objects': queryset})

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('print/<int:object_id>/', self.admin_site.admin_view(self.print_view), name='print_view'),
        ]
        return my_urls + urls

admin.site.register(Problems, ProblemsAdmin)
