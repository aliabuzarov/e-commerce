from django.urls import path
from .views import index, contact, error, coming_soon, ContactView


urlpatterns = [
    path('',index, name='home' ),
    path('about/', ContactView.as_view(), name='contact'),
    path('error/', error, name='404'),
    path('coming-soon/', coming_soon, name='soon'),




]