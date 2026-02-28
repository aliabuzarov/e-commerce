from product.models import Product
from core.models import Subscribe
from django.http import JsonResponse
from product.api.serializers import ProductSerializer, ProductCreateSerializer, SubscribeSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView

class SubscribeCreateAPIView(CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

@api_view(http_method_names=['POST', 'GET'])
def products(request):
    products = Product.objects.all()
    if request.method == 'POST':
        serilaizer = ProductCreateSerializer(data = request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(data= serilaizer.data, safe=False)
        return JsonResponse(data= serilaizer.errors, safe=False)
    serilaizer = ProductSerializer(products, context = {'request' : request}, many = True)
    return JsonResponse(data= serilaizer.data, safe=False)

@api_view(http_method_names=['PUT', 'PATCH'])
def product_update(request,pk):
    product = Product.objects.get(id = pk)
    if request.method == 'PUT':
        serilaizer = ProductCreateSerializer(instance = product, data = request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(data= serilaizer.data, safe=False)
        return JsonResponse(data= serilaizer.errors, safe=False)
    serilaizer = ProductSerializer(products, context = {'request' : request}, many = True)
    return JsonResponse(data= serilaizer.data, safe=False)

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()