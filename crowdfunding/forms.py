from django import forms
from .models import Pledge


class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['reward']