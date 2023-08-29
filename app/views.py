from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from . import models
from . import serializers


# Create your views here.
class Product(APIView):
    def get(self, request, id=None, category_title=None):
        if id:
            try:
                product = models.Product.objects.get(id=id)
                serialized_product = serializers.SerializedProduct(product)
                return Response(serialized_product.data, status=status.HTTP_200_OK)
            except:
                return Response({"msg": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        elif category_title:
            category = models.Category.objects.get(title=category_title)
            products = models.Product.objects.get(category=category)
            serialized_products = serializers.SerializedProduct(products)
            return Response(serialized_products.data, status=status.HTTP_200_OK)
        else:
            title = request.query_params.get('title')
            min_price = request.query_params.get('min_price')
            max_price = request.query_params.get('max_price')
            products = models.Product.objects.all()
            if title:
                products = products.filter(title__icontains=title)
            if min_price:
                products = products.filter(price__gte=min_price)
            if max_price:
                products = products.filter(price__lte=max_price)
            serialized_products = serializers.SerializedProduct(products, many=True)
            return Response(serialized_products.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_product = serializers.SerializedProduct(data=request.data)
        if serialized_product.is_valid():
            serialized_product.save()
            products = models.Product.objects.all()
            serialized_products = serializers.SerializedProduct(products, many=True)
            return Response(serialized_products.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Product not added"}, status=status.HTTP_400_BAD_REQUEST)


class Customer(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        surname = request.query_params.get('surname')
        customers = models.Customer.objects.all()
        if name:
            customers = customers.filter(name__icontains=name)
        if surname:
            customers = customers.filter(surname__icontains=surname)
        serialized_customers = serializers.SerializedCustomer(customers, many=True)
        return Response(serialized_customers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_customer = serializers.SerializedCustomer(data=request.data)
        if serialized_customer.is_valid():
            serialized_customer.save()
            customers = models.Customer.objects.all()
            serialized_customers = serializers.SerializedCustomer(customers, many=True)
            return Response(serialized_customers.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Product not added"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        serialized_customer = serializers.SerializedCustomer(data=request.data, partial=True)
        if serialized_customer.is_valid():
            serialized_customer.save()
            customers = models.Customer.objects.all()
            serialized_customers = serializers.SerializedCustomer(customers, many=True)
            return Response(serialized_customers.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Product not added"}, status=status.HTTP_400_BAD_REQUEST)


class Manager(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        surname = request.query_params.get('surname')
        managers = models.Manager.objects.all()
        if name:
            managers = managers.filter(name__icontains=name)
        if surname:
            managers = managers.filter(surname__icontains=surname)
        serialized_managers = serializers.SerializedManager(managers, many=True)
        return Response(serialized_managers.data, status=status.HTTP_200_OK)


class Cart(APIView):
    def get(self, request, customer_id):
        cart_items = models.Cart.objects.filter(customer_id=customer_id)
        serialized_cart = serializers.SerializedCart(cart_items, many=True)
        return Response({"cart": serialized_cart.data}, status=status.HTTP_200_OK)


class DeliveryCrew(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        surname = request.query_params.get('surname')
        delivery_crew = models.DeliveryCrew.objects.all()
        if name:
            delivery_crew = delivery_crew.filter(name__icontains=name)
        if surname:
            delivery_crew = delivery_crew.filter(surname__icontains=surname)
        serialized_delivery_crew = serializers.SerializedDeliveryCrew(delivery_crew, many=True)
        return Response(serialized_delivery_crew.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category(request):
    match request.method:
        case 'GET':
            categories = models.Category.objects.all()
            serialized_category = serializers.SerializedCategory(categories, many=True)
            return Response(serialized_category.data, status=status.HTTP_200_OK)
        case 'POST':
            serialized_category = serializers.SerializedCategory(data=request.data)
            if serialized_category.is_valid():
                serialized_category.save()
                category = models.Category.objects.all()
                serialized_category = serializers.SerializedCategory(category, many=True)
                return Response(serialized_category.data, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "Category not added"}, status=status.HTTP_400_BAD_REQUEST)
