from rest_framework.serializers import ModelSerializer, IntegerField

from . import models


class SerializedProduct(ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price', 'image', 'description']


class SerializedCart(ModelSerializer):
    product = SerializedProduct(read_only=True)
    product_id = IntegerField(write_only=True)

    class Meta:
        model = models.Cart
        fields = ['id', 'customer', 'product', 'quantity', 'product_id']


class SerializedCustomer(ModelSerializer):
    cart = SerializedCart(read_only=True)

    class Meta:
        model = models.Customer
        fields = ['id', 'name', 'surname', 'image', 'birthday', 'cart']


class SerializedManager(ModelSerializer):
    class Meta:
        model = models.Manager
        fields = ['id', 'name', 'surname', 'image', 'birthday']


class SerializedDeliveryCrew(ModelSerializer):
    class Meta:
        model = models.DeliveryCrew
        fields = ['id', 'name', 'surname', 'image', 'birthday']
