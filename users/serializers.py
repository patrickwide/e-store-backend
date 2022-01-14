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

    class Meta:
        model = Product
        fields = ['id','productName','productDescription','owner']

