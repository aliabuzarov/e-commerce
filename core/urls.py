from django.urls import path
from .views import index, contact


urlpatterns = [
    path('',index, name='home' ),
    path('about/', contact, name='contact')



]