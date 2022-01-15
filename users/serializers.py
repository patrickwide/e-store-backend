# django imports
from django.db.models import fields

# rest_framework imports
from rest_framework import serializers

# shops database imports
from shops.models import Product


class ProductSerializer(serializers.ModelSerializer):
    productName = serializers.CharField(max_length=64)
    productDescription = serializers.CharField(max_length=64)
    owner = serializers.ReadOnlyField(source='owner.username')
    productCategoryId = serializers.ReadOnlyField(source='productCategoryId.productCategory')
    productPhoto1 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 ) 
    productPhoto2 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto3 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto4 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto5 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )

    class Meta:
        model = Product
        fields = ['id','productName','productCategoryId','productDescription','owner', 'productPhoto1', 'productPhoto2', 'productPhoto3', 'productPhoto4', 'productPhoto5' ]

