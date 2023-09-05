from rest_framework import serializers
from grocery.models import (
    Category,
    Product,
    CartItem,
)


class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'name', 'slug', 'image',
            'parent_category',
        ]

    def get_parent_category(self, obj):
        if obj.parent is not None:
            parent_id = obj.parent.id
            if parent_id is not None:
                try:
                    category = Category.objects.get(id=parent_id)
                    return category.name
                except Category.DoesNotExist:
                    return None
        return None


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            'name', 'slug', 'category',
            'price', 'image_large',
            'image_medium', 'image_small'
        ]


class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product_name', 'quantity']

    def get_product_name(self, obj):
        return obj.product.name


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def create(self, validated_data):
        user = self.context['request'].user
        cart_item = CartItem.objects.create(user=user, **validated_data)
        return cart_item
