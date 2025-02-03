from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('cart/', cart),
    path('add/', product_add),
    path('products/', product_list),
    path('products/<str:id>/', product_page),
]