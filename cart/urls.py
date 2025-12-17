from django.urls import path
from .views import my_cart, empty_cart


urlpatterns = [
    path('empty_cart/', empty_cart, name='empty'),
    path('mycart/', my_cart, name='cart'),


]