from django import forms

from musician.models import Musicians

class Musician_form(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'