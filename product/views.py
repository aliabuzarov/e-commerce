from django.shortcuts import render


# Create your views here.
def details(request):
    return render(request, 'product-details.html')

def details_product(request):
    return render(request, 'shop-left-sidebar.html')