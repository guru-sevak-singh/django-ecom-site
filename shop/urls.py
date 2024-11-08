from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_info/<int:id>', views.detail, name='product_info'),
    path('cart', views.cart, name='cart'),
]