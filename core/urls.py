from django.urls import path
from .views import index, contact, error, coming_soon


urlpatterns = [
    path('',index, name='home' ),
    path('about/', contact, name='contact'),
    path('error/', error, name='404'),
    path('coming-soon', coming_soon, name='soon'),




]