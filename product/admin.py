from django.contrib import admin
from .models import Product, Category, Order, Review,ProductImage
from modeltranslation.admin import  TranslationAdmin

class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(ProductImage)

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cover_image', 'stock', 'category']
    list_editable = ['stock', 'category']
    list_filter =  ['id', 'category', 'stock']
    list_display_links = ['id', 'title']
    readonly_fields = ['price']
    search_fields = ['title', 'id', 'category']
    inlines = [ProductImageInline]
    
    
