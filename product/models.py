from django.db import models
from core.models import AbstarctModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Category(AbstarctModel):
    parent = models.ForeignKey('self', related_name='child', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=100)
    description = models.TextField('description', blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} / {self.name}'
        else:
            return f'{self.name}'
        
    class Meta:
        verbose_name_plural = 'Categories'



class Product(AbstarctModel):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('title', max_length=200)
    description = models.TextField('description')
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('stock', default=0)
    cover_image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title


    class Meta:
        ordering = ("-created_at",)

    
class Order(AbstarctModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField('quantity', default=1)
    total_price = models.DecimalField('total price', max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Order #{self.id} - {self.product.title}"
    
class Review(AbstarctModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField('rating')
    comment = models.TextField('comment', blank=True)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Review for {self.product.title} - {self.rating} stars - by {self.user}"
    
class ProductImage(AbstarctModel):
    image = models.ImageField('product_images/')
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title}'