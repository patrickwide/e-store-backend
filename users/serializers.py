# django imports
from django.db.models import fields

# rest_framework imports
from rest_framework import serializers

# shops database imports
from database.models import *

# users
from django.contrib.auth.models import User



class ProductSerializer(serializers.ModelSerializer):

    shop = serializers.ReadOnlyField( source='shop.name' )
    name = serializers.CharField( max_length=64 )
    price = serializers.IntegerField()
    category = serializers.ReadOnlyField( source='category.name' )
    description = serializers.CharField( max_length=500 )
    photo1 = serializers.FileField( max_length=255 ) 
    photo2 = serializers.FileField( max_length=255 )
    photo3 = serializers.FileField( max_length=255 )
    photo4 = serializers.FileField( max_length=255 )
    photo5 = serializers.FileField( max_length=255 )

    class Meta:
        model = Product
        fields = ['id','shop','name','price','category','description','photo1', 'photo2', 'photo3', 'photo4', 'photo5' ]


class ShoppingCacheSerializer(serializers.ModelSerializer):

    class Meta:
        model = shoppingCache
        fields = '__all__'


class purchaseSerializer(serializers.ModelSerializer):
    # product = serializers.CharField( source='shop.name' )
    product = ProductSerializer(read_only=True, many=False)
    user = serializers.ReadOnlyField( source='user.username' )
    class Meta:
        model = Order
        fields = '__all__'


    def create(self, validated_data):
        return Order.objects.create(**validated_data)









