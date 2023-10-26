from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'description', 'count', 'date_of_issue', 'year_of_publication')
        labels = {
            'name': 'Назва книги',
            'author': 'Автор',
            'description': 'Опис',
            'count': 'Оцінка',
            'date_of_issue': 'Дата випуску',
            'year_of_publication': 'Дата публікації',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date_of_issue': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }
            ),
            'year_of_publication': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }
            )        }
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # self.fields['position'].empty_label = "Select"
