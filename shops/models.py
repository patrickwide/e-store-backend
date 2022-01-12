from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=64)
    productDescription = models.CharField(max_length=64)
    owner = models.ForeignKey('auth.User',default=1, related_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"productId => {self.id} : productName => {self.productName}, productDescription => {self.productDescription}."

