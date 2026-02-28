from django.db import models
from core.models import AbstarctModel
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()
# Create your models here.


class Basket(AbstarctModel):

    user = models.ForeignKey(User, related_name="baskets", on_delete= models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username}'

class BasketItem(AbstarctModel):
    basket = models.ForeignKey(Basket, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title}'