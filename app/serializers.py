from rest_framework.serializers import ModelSerializer, IntegerField, PrimaryKeyRelatedField

from . import models


class SerializedCategory(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class SerializedProduct(ModelSerializer):
    category = SerializedCategory(read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price', 'image', 'description', 'category']


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
