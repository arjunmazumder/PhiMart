from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from product.views import ProductModelViewSet, CategoryModelViewSet

router.register('products', ProductModelViewSet)
router.register('categories', CategoryModelViewSet)

urlpatterns = router.urls
    
# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.category_urls')),   
# ]




