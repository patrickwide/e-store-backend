from django.db.models import fields
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    productName = serializers.CharField(max_length=64)
    productDescription = serializers.CharField(max_length=64)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.productName = validated_data.get('productName', instance.productName)
        instance.productDescription = validated_data.get('productDescription', instance.productDescription)
        
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'Product']