from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label= "Имя", initial="undefined")
    age = forms.IntegerField(label="Возраст", widget=forms.Textarea, initial= 22)

