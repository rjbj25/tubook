from django.http import HttpResponse
from django.shortcuts import render

def shop(request):
    return render(request,'shop/base.html')
