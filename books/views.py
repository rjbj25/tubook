from django.shortcuts import render
def create_book(request):
    return render(request,'books/books_maker.html')