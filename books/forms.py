from django import froms
from books.models import Book

class BookForm(forms.ModelForm):
    model = Book