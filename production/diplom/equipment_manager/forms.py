from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['name', 'description', 'serial_number', 'assigned_user', 'location']
