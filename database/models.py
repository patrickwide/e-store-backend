from django.db import models
from django.db.models.deletion import CASCADE

# create user auth Token imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import datetime
from django.utils import timezone

# Create your models here.
# class users ->>>

# app account
class Shop(models.Model):
    user = models.ForeignKey( 'auth.User', related_name='Shop_user' , on_delete=models.CASCADE )
    name = models.CharField( max_length=64  )
    profile = models.FileField( upload_to='pictures/%Y/%m/%d' , max_length=255 )
    shopBio = models.CharField( max_length=255 )
    location = models.CharField( max_length=255  )
    rated = models.IntegerField( default=3  )

    def __str__(self):
        return f"{self.id} {self.name} {self.user}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=64  )

    def __str__(self):
        return f"{self.id} {self.name}"

class Product(models.Model):
    shop = models.ForeignKey( Shop , on_delete=models.CASCADE, related_name='Product_shop' )
    name = models.CharField( max_length=64 )
    price = models.IntegerField()
    category = models.ForeignKey( ProductCategory, on_delete=CASCADE , related_name='Product_category' )
    description = models.CharField( max_length=500 )
    photo1 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 ) 
    photo2 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    photo3 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    photo4 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    photo5 = models.FileField( upload_to='pictures/%Y/%m/%d' , default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )

    def __str__(self):
        return f"{self.id} {self.name}"



# web account
class Notification(models.Model):
    user = models.ForeignKey( 'auth.User', related_name='Notification_user' , on_delete=models.CASCADE )
    newsLetter = models.BooleanField()
    productUpdate = models.BooleanField()
    productLaunch = models.BooleanField()
    
    def __str__(self):
        return f"{self.id} {self.user}"
    
class shoppingCache(models.Model):
    user = models.ForeignKey( 'auth.User', related_name='shoppingCache_user' , on_delete=models.CASCADE )
    phone = models.CharField( max_length=15 )
    mpesa = models.CharField( max_length=15 )
    location = models.CharField( max_length=250 )

class Order(models.Model):
    user = models.ForeignKey( 'auth.User', related_name='Order_buyer' , on_delete=models.CASCADE )
    product = models.ForeignKey( Product , on_delete=CASCADE , related_name='Order_product' )
    date = models.DateField( auto_now_add=timezone.now() ) 
    note = models.CharField( max_length=255 )

# create_auth_token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create( user=instance )

# create_default_notifications
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_notifications(sender, instance=None, created=False, **kwargs):
    if created:
        Notification.objects.create( user=instance, newsLetter=True , productUpdate=True , productLaunch=True )

# create_default_shoppingCache
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_shoppingCache(sender, instance=None, created=False, **kwargs):
    if created:
        shoppingCache.objects.create( user=instance, phone="+254-123-456-7" , mpesa="+254-123-456-7" , location="0000-0000" )


