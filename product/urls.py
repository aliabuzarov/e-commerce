from django.urls import path
from .views import details, ShopViewList,ShopDetailView


urlpatterns = [
    path('shop/',ShopViewList.as_view() , name='details'),
    path('shop/<str:slug>/', ShopDetailView.as_view(), name='product'),


]   
