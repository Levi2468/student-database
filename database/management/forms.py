from django import forms
from .models import Details


class Formfield(forms.ModelForm):
    class Meta:
        model=Details
        fields = ["Roll_no","name"]
