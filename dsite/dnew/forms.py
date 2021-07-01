from django import forms
from .models import Person, User

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = ["name", "email", "mobile"]
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'