from django.urls import path
from .views import details, details_product


urlpatterns = [
    path('product/', details, name='product'),
    path('details/', details_product, name='details'),


]