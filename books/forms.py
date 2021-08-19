from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
    model = Book