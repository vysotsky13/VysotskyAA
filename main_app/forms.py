from django import forms
from .models import ResponseModel


class ResponseForm(forms.ModelForm):
    class Meta:
        model = ResponseModel
        fields = '__all__'
