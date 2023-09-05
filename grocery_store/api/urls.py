from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView,
    ProductListView,
    CartItemViewSet,
)

app_name = 'api'
router = DefaultRouter()
router.register(r'cartitems', CartItemViewSet, basename='cart')
urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartItemViewSet.as_view({'get': 'cart_summary'}), name='cart-summary'),
    path('api-token-auth/', views.obtain_auth_token),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
]
