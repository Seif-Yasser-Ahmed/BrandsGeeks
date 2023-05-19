from django.db import models
from django.contrib.auth.models import User
import uuid


class Product(models.Model):
    categories = [
        ('Hoodie', 'Hoodie'),
        ('Cargo', 'Cargo'),
        ('Jeans', 'Jeans'),
        ('Oversize', 'Oversize'),
        ('Jacket', 'Jacket'),
    ]
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=1)
    image = models.ImageField(upload_to='images/%y/%m')
    active = models.BooleanField(default=True)
    category = models.CharField(
        max_length=100, null=True, blank=True, choices=categories)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=1, null=True, blank=True)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, default=1, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name

# # class Hoodie(models.Model):
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=1)
#     image = models.ImageField(upload_to='images/%y/%m')
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']
#
# class Cargo(models.Model):
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=1)
#     image = models.ImageField(upload_to='images/%y/%m')
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class Jean(models.Model):
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=1)
#     image = models.ImageField(upload_to='images/%y/%m')
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class Oversize(models.Model):
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=1)
#     image = models.ImageField(upload_to='images/%y/%m')
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class Jacket(models.Model):
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=1)
#     image = models.ImageField(upload_to='images/%y/%m')
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class RegUser(models.Model):
#     Firstname = models.CharField(max_length=50)
#     Lastname = models.CharField(max_length=50)
#     Email = models.CharField(max_length=50)
#     Contact = models.CharField(max_length=50)
#     Password = models.CharField(max_length=50)
