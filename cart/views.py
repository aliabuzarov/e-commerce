from django.shortcuts import render

# Create your views here.
def empty_cart(request):
    return render(request, 'empty-cart.html')

def my_cart(request):
    return render(request, 'my-cart.html')