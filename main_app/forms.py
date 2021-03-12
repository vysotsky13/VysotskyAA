from django import forms
from .models import ResponseModel, BookModel, ClientsHistoryModel, Order


class ResponseForm(forms.ModelForm):
    class Meta:
        model = ResponseModel
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ClientsHistoryForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=BookModel.objects.all(), empty_label=None, label='Книга', disabled=True)

    class Meta:
        model = ClientsHistoryModel
        fields = ('book', 'full_name', 'date_of_issue', 'return_date')
