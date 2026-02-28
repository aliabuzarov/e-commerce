from django import template
register = template.Library()
from product.models import Product


@register.simple_tag
def get_products(limit):
    return Product.objects.all()[:limit]