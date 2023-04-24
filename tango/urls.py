from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('product-detail/<str:pk>', views.about_product),
    path('current-category/<str:pk>', views.about_product),
    path('search-products', views.search_for_products),
    path('add-product/<int>:pk', views.add_product_to_cart)

]
