from django.db.models import fields
from rest_framework import serializers
from database.models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='shop.shopName')
    # productOwner = serializers.ReadOnlyField(source='productOwner.username')
    name = serializers.CharField( max_length=64 )
    price = serializers.IntegerField( default=0 )
    category = serializers.CharField( source='productCategory.productCategoryName' )
    description = serializers.CharField( max_length=500 )
    photo1 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 ) 
    photo2 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    photo3 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    photo4 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    photo5 = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )


    # shop = serializers.ReadOnlyField( source='Shop.name' )
    # name = serializers.CharField( max_length=64 )
    # price = serializers.IntegerField()
    # category = serializers.ReadOnlyField( source='Category.ProductCategory' )
    # description = serializers.CharField( max_length=500 )
    # photo1 = serializers.FileField( max_length=255 ) 
    # photo2 = serializers.FileField( max_length=255 )
    # photo3 = serializers.FileField( max_length=255 )
    # photo4 = serializers.FileField( max_length=255 )
    # photo5 = serializers.FileField( max_length=255 )


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
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.photo1 = validated_data.get('photo1', instance.photo1)
        instance.photo2 = validated_data.get('photo2', instance.photo2)
        instance.photo3 = validated_data.get('photo3', instance.photo3)
        instance.photo4 = validated_data.get('photo4', instance.photo4)
        instance.photo5 = validated_data.get('photo5', instance.photo5)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = ['id','shop','name','price','category','description','photo1', 'photo2', 'photo3', 'photo4', 'photo5' ]


class shopSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField( source='user.username' )
    name = serializers.CharField( max_length=64 )
    profile = serializers.FileField( default="/media/pictures/2022/01/08/project-2.jpg" , max_length=255 )
    shopBio = serializers.CharField( max_length=255 )
    location = serializers.CharField( max_length=255 )
    rated = serializers.IntegerField()


    def create(self, validated_data):
        return Shop.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.shopBio = validated_data.get('shopBio', instance.shopBio)
        instance.location = validated_data.get('location', instance.location)
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

        