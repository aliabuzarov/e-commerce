from django.urls import path
from product.api.views import products, product_update, ProductListAPIView, SubscribeCreateAPIView

urlpatterns = [
    
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/<int:pk>/', product_update, name='product_update'),
    path('subscriber/',SubscribeCreateAPIView.as_view(), name='subscriber' )
]    