from django.urls import path
from .views import blog, blog_details


urlpatterns = [

    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog_details'),


]