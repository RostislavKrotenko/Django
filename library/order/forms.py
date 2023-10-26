from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('book', 'plated_end_at')
        labels = {
            'book': 'Книга',
            'plated_end_at': 'Дата повернення',
        }
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'plated_end_at': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }
            )
        }