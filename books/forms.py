from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
    model = Book
    
    class Meta:

        model = Book
        fields = (
            'format_form', 
            'cover_type', 
            'union_type', 
            'cover', 
            'have_sub_cover', 
            'sub_cover', 
            'sheets_quantity', 
            'sheets_type'
        )
        