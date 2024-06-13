from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.urls import path
from django.shortcuts import render
from .models import Problems

class UserFilter(admin.SimpleListFilter):
    title = 'Пользователь'
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        return [(user.id, user.username) for user in User.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__id=self.value())
        return queryset

class StatusFilter(admin.SimpleListFilter):
    title = 'Статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [(status, status) for status in Problems.STATUS_CHOICES]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset

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

    list_filter = (UserFilter, StatusFilter)

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
