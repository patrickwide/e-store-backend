# django imports
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import authentication
from rest_framework import permissions
from django.contrib.auth.models import User
# rest_framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# shops database imports
from shops.models import Product

# serializers imports
from .serializers import ProductSerializer


# Create your views here.
class apiOverview(APIView):
    def get(self, req):
        if req.method == "GET":

            data = {
                'channel':'/users/..',
                'List':'/product-list/',
                'Detail View':'/product-detail/<str:pk>/',
                # 'Create':'/product-create/',
                # 'Update':'/product-update/<str:pk>/',
                # 'Delete':'/product-delete/<str:pk>/',
            }

            return Response(data=data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class productList(APIView):
    def get(self, req):
        if req.method == "GET":

            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productDetail(APIView):
    def get(self, req, pk):
        if req.method == "GET":

            product = get_object_or_404(Product,id=pk)
            serializer = ProductSerializer(product,many=False)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.width(2)
# t.speed(15)

# col = ("white","pink","cyan")
# for i in range(300):
#     t.pencolor(col[i%3])
#     t.forward(i*4)
#     t.right(121)

# while(True):
#     print("Running...")