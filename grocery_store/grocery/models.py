from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_images/')

    verbose_name = 'category'
    verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='subcategory_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    verbose_name = 'subcategory'
    verbose_name_plural = 'subcategories'

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    image_large = models.ImageField(upload_to='product_images/large/')
    image_medium = models.ImageField(upload_to='product_images/medium/')
    image_small = models.ImageField(upload_to='product_images/small/')

    def __str__(self):
        return self.name
