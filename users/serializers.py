# django imports
from django.db.models import fields

# rest_framework imports
from rest_framework import serializers

# shops database imports
from database.models import *


class ProductSerializer(serializers.ModelSerializer):

    shopName = serializers.ReadOnlyField( source='shop.shopName' )
    productName = serializers.CharField( default='N/A' , max_length=64 )
    productPrice = serializers.IntegerField( default=0 )
    productCategory = serializers.ReadOnlyField( source='productCategory.productCategoryName' )
    productDescription = serializers.CharField( default='N/A' , max_length=500 )
    productPhoto1 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 ) 
    productPhoto2 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto3 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto4 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto5 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )

    class Meta:
        model = Product
        fields = ['id','shopName','productName','productPrice','productCategory','productDescription','productPhoto1', 'productPhoto2', 'productPhoto3', 'productPhoto4', 'productPhoto5' ]
