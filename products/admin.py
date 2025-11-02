from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'unit', 'available', 'featured', 'stock_quantity', 'date_added')
    list_filter = ('category', 'available', 'featured')  # Add featured to filters
    search_fields = ('name', 'description')
    ordering = ('category', 'name')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'price', 'unit', 'stock_quantity', 'image', 'available', 'featured')  # Add featured here
        }),
        ('Date Info', {
            'fields': ('date_added',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('date_added',)
