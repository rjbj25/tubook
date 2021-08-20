from books.forms import BookForm
from django.shortcuts import render, redirect
from books.forms import BookForm

def create_book(request):
    if request.method=='POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = BookForm()
    return render(
        request=request,
        template_name='books/books_maker.html',
        context={
            'form':form
        }
    )