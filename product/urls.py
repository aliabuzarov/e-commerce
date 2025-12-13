from django.urls import path
from .views import details


urlpatterns = [
    path('product/', details, name='product'),


]