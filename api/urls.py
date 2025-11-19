from django.urls import path, include
from product.views import ProductModelViewSet, CategoryModelViewSet, ReviewModelViewSet
from order.views import CartViewSet, CartItemViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductModelViewSet)
router.register('categories', CategoryModelViewSet)
router.register('carts', CartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewModelViewSet, basename='product-review')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

# urlpatterns = router.urls
    
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('products/', include('product.product_urls')),
    # path('categories/', include('product.category_urls')),   
]




