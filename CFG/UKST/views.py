from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'UKST/home.html')
    return HttpResponse('<h1>hi</h1>')

def about(request):
    return render(request, 'UKST/about.html')
