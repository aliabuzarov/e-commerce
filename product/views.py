from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView

# Create your views here.
def details(request,pk):
    product = Product.objects.get(id = pk)
    context = {

        'product': product
        }
    return render(request, 'product-details.html', context)

class ShopDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'

class ShopViewList(ListView):
    template_name = 'shop-left-sidebar.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = categories = Category.objects.all()
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('category')
        if cat_id:
            queryset = queryset.filter(category = cat_id)
        return queryset


