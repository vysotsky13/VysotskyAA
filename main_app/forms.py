from django import forms
from .models import ResponseModel, BookModel


class ResponseForm(forms.ModelForm):
    class Meta:
        model = ResponseModel
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
