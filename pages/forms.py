from django import forms
from .models import bookTables

class bookTablesForm(forms.ModelForm):
    class Meta:
        model = bookTables
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-sm-20', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-sm-20', 'placeholder': 'Email'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control col-sm-20', 'placeholder': 'Guests'}),
            'date': forms.DateInput(attrs={'class': 'form-control col-sm-20', 'placeholder': 'Date (YYYY-MM-DD)'}),
            'time': forms.TimeInput(attrs={'class': 'form-control col-sm-20', 'placeholder': 'Time'}),
        }