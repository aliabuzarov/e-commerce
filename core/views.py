from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def error(request):
    return render(request,'404.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')