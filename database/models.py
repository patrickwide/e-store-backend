from django.db import models
from django.db.models.deletion import CASCADE

# create user auth Token imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
# class users ->>>

class Shop(models.Model):
    shopOwner = models.ForeignKey( 'auth.User', related_name='shopOwner' , on_delete=models.CASCADE )
    shopName = models.CharField( max_length=64 )
    shopProfile = models.FileField( upload_to='pictures/%Y/%m/%d' , max_length=255 )
    shopBio = models.CharField( max_length=255 )
    shopLocation = models.CharField( max_length=255 )

    def __str__(self):
        return f"{self.id} {self.shopName} {self.shopOwner}"

class ProductCategory(models.Model):
    productCategoryName = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.productCategoryName}"

class Product(models.Model):
    shop = models.ForeignKey( Shop , default="None" , on_delete=models.CASCADE, related_name='shop' )
    productName = models.CharField( max_length=64 )
    productPrice = models.IntegerField()
    productCategory = models.ForeignKey( ProductCategory , on_delete=CASCADE , related_name='productCategory' )
    productDescription = models.CharField( max_length=500 )
    productPhoto1 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 ) 
    productPhoto2 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto3 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto4 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto5 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )

    def __str__(self):
        return f"{self.id} {self.productName}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create( user=instance )

# Product.objects.create(shop,productName,productPrice,productCategory,productDescription,productPhoto1,productPhoto2)