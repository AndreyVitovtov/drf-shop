from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('products/', views.Product.as_view()),
    path('product/<int:id>', views.Product.as_view()),
    path('products-by-category/<str:category_title>', views.Product.as_view()),
    path('customers/', views.Customer.as_view()),
    path('managers/', views.Manager.as_view()),
    path('cart/<int:customer_id>', views.Cart.as_view()),
    path('categories/', views.category),
    path('auth', auth_views.obtain_auth_token)
]
