from django.contrib import admin
from .models import Category, Subcategory, Product


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    prepopulated_fields = {'slug': ('name',)}
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    prepopulated_fields = {'slug': ('name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

