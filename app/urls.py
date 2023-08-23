from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.Product.as_view()),
    path('product/<int:id>', views.Product.as_view()),
    path('customers/', views.Customer.as_view()),
    path('managers/', views.Manager.as_view()),
    path('cart/<int:customer_id>', views.Cart.as_view()),
]
