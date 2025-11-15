from django.urls import path, include
from product.views import ProductModelViewSet, CategoryModelViewSet, ReviewModelViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductModelViewSet)
router.register('categories', CategoryModelViewSet)

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewModelViewSet, basename='product-review')

# urlpatterns = router.urls
    
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls))
    # path('products/', include('product.product_urls')),
    # path('categories/', include('product.category_urls')),   
]




