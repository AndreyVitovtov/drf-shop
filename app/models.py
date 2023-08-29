from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.price}$"


class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product}: {self.quantity}pc."


class Manager(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class DeliveryCrew(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"
