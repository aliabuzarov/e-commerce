from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField('title', max_length=200)
    description = models.TextField('description')
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('stock', default=0)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField('name', max_length=100)
    description = models.TextField('description', blank=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField('quantity', default=1)
    total_price = models.DecimalField('total price', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    def __str__(self):
        return f"Order #{self.id} - {self.product.title}"
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField('rating')
    comment = models.TextField('comment', blank=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    def __str__(self):
        return f"Review for {self.product.title} - {self.rating} stars"