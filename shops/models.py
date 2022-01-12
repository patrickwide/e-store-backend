from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=64)
    productDescription = models.CharField(max_length=64)

    def __str__(self):
        return f"productId => {self.id} : productName => {self.productName}, productDescription => {self.productDescription}."

