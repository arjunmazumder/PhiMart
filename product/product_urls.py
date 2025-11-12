from django.urls import path
from product import views

urlpatterns = [
    path('', views.view_products, name='view-all-products'),
    path('<int:pk>/', views.view_specific_product, name='view-specific-product')

]