from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField(max_length=250, unique=True, null=False, blank=False)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]

    registration_method = models.CharField(
        max_length=10,
        choices=REGISTRATION_CHOICES,
        default='email'
    )

    REQUIRED_FIELDS = []

    def __str__(self):
       return f'{self.first_name} {self.last_name} ({self.email})'


class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=256)
    price = models.FloatField()

class Product(models.Model):
    product = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    quantity = models.CharField(max_length=100, null=False, blank=False)
    standardized_quantity = models.CharField(max_length=100, null=False, blank=False)
    store = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: ${self.price}, Standardized Quantity: {self.standardized_quantity}, Store: {self.store}"

