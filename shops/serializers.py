from django.db.models import fields
from rest_framework import serializers
from database.models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='shop.shopName')
    # shop = serializers.CharField( source='shop.shopName' )
    productOwner = serializers.ReadOnlyField(source='productOwner.username')
    productName = serializers.CharField( max_length=64 )
    productPrice = serializers.IntegerField( default=0 )
    productCategory = serializers.CharField( source='productCategory.productCategoryName' )
    productDescription = serializers.CharField( max_length=500 )
    productPhoto1 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 ) 
    productPhoto2 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto3 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto4 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    productPhoto5 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Product` instance, given the validated data.
    #     """
    #     print(validated_data)
    #     return  Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.productName = validated_data.get('productName', instance.productName)
        instance.productPrice = validated_data.get('productPrice', instance.productPrice)
        instance.productCategory = validated_data.get('productCategory', instance.productCategory)
        instance.productDescription = validated_data.get('productDescription', instance.productDescription)
        instance.productPhoto1 = validated_data.get('productPhoto1', instance.productPhoto1)
        instance.productPhoto2 = validated_data.get('productPhoto2', instance.productPhoto2)
        instance.productPhoto3 = validated_data.get('productPhoto3', instance.productPhoto3)
        instance.productPhoto4 = validated_data.get('productPhoto4', instance.productPhoto4)
        instance.productPhoto5 = validated_data.get('productPhoto5', instance.productPhoto5)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = ['id','shopName','productOwner','productName','productPrice', 'productCategory','productDescription','productPhoto1','productPhoto2','productPhoto3','productPhoto4','productPhoto5']

class shopSerializer(serializers.ModelSerializer):
    shopOwner = serializers.ReadOnlyField( source='shopOwner.username' )
    shopName = serializers.CharField( max_length=64 )
    shopProfile = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    shopBio = serializers.CharField( max_length=255 )
    shopLocation = serializers.CharField( max_length=255 )

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.shopName = validated_data.get('shopName', instance.shopName)
        instance.shopProfile = validated_data.get('shopProfile', instance.shopProfile)
        instance.shopBio = validated_data.get('shopBio', instance.shopBio)
        instance.shopLocation = validated_data.get('shopLocation', instance.shopLocation)
        instance.save()
        return instance

    class Meta:
        model = Shop
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'Product']


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input-type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username','password','password2']

        extra_kwargs = {
            'password': { 'write_only':True }
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'error - password do not match'})
        user.set_password(password)
        user.save()
        return user

        