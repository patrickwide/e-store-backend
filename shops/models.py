from django.db import models
from django.db.models.deletion import CASCADE

# create user auth Token imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class ProductCategory(models.Model):
    productCategory = models.CharField(max_length=64)

    def __str__(self):
        return f"id : {self.id},productCategory : {self.productCategory}"

class Product(models.Model):
    owner = models.ForeignKey('auth.User',default=1, related_name='ProductOwner', on_delete=models.CASCADE)
    productName = models.CharField(max_length=64)
    productDescription = models.CharField(max_length=500)
    productCategoryId = models.ForeignKey(ProductCategory,on_delete=CASCADE, related_name='Category', default=1)
    productPhoto1 = models.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , upload_to='pictures/%Y/%m/%d' , max_length=255 , null=False , blank=False ) 
    productPhoto2 = models.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , upload_to='pictures/%Y/%m/%d' , max_length=255 , null=False , blank=False )
    productPhoto3 = models.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , upload_to='pictures/%Y/%m/%d' , max_length=255 , null=False , blank=False )
    productPhoto4 = models.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , upload_to='pictures/%Y/%m/%d' , max_length=255 , null=False , blank=False )
    productPhoto5 = models.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , upload_to='pictures/%Y/%m/%d' , max_length=255 , null=False , blank=False )

    def __str__(self):
        return f"productId : {self.id}, productName : {self.productName}."


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
