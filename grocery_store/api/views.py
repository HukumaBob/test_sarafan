from django.db.models import Sum
from rest_framework import generics, status, viewsets
from grocery.models import (
    Category,
    Product,
    CartItem,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .pagination import CustomPagination
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CartItemSerializer, CartSerializer,
)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPagination


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        # Add processing for the "?clear=true" request parameter to remove all cart items
        clear_cart = request.query_params.get('clear', None)
        if clear_cart:
            user = request.user
            CartItem.objects.filter(user=user).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # If the "clear" parameter is not specified, return the shopping list
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data

        existing_item = CartItem.objects.filter(user=self.request.user, product=data.get('product')).first()

        if existing_item:
            existing_item.quantity += data.get('quantity')
            existing_item.save()
            serializer = self.get_serializer(existing_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def cart_summary(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_cost = sum(item.product.price * item.quantity for item in cart_items)

        data = {
            'total_quantity': total_quantity,
            'total_cost': total_cost,
            'cart_items': CartSerializer(cart_items, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)
