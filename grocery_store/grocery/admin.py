from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
