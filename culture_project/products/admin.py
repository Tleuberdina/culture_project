from django.contrib import admin

from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'text',
        'author',
        'created'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'estimation',
    )
    search_fields = ('text',)
    list_filter = ('text',)
    list_display_links = ('text',)

admin.site.empty_value_display = 'Не задано'
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
