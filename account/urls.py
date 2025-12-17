from django.urls import path
from .views import signin, signup, wish_list


urlpatterns = [

    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('wishlist/', wish_list, name='wishlist'),



]