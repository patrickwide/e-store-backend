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

# database imports
from .models import Product

# serializers imports
from .serializers import ProductSerializer

# permissions imports
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class apiOverview(APIView):
    def get(self, req):
        if req.method == "GET":

            data = {
                'channel':'/shops/..',
                'List':'/product-list/',
                'Detail View':'/product-detail/<str:pk>/',
                'Create':'/product-create/',
                'Update':'/product-update/<str:pk>/',
                'Delete':'/product-delete/<str:pk>/',
            }

            return Response(data=data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productList(APIView):
    # prevent unauthenticated users from accessing the data
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, req):
        if req.method == "GET":
            
            # filter the data and give users data only
            products = Product.objects.filter(owner=req.user)
            serializer = ProductSerializer(products,many=True)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productDetail(APIView):
    # prevent unauthenticated users from accessing the data
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, req, pk):
        if req.method == "GET":
            # get only data by id and also data that is created by the user
            product = get_object_or_404(Product,id=pk,owner=req.user)
            serializer = ProductSerializer(product,many=False)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class productCreate(APIView):
    # prevent unauthenticated users from creating new products
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, req):
        if req.method == "POST":
            
            serializer = ProductSerializer(data=req.data)
            if serializer.is_valid():
                serializer.save(owner=req.user)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productUpdate(APIView):
    # only if the user created the data is allowed to update
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def put(self, req, pk):
        if req.method == "PUT":

            product = get_object_or_404(Product,id=pk)
            # check if user have permission to update the data
            self.check_object_permissions(req, product)
            serializer = ProductSerializer(instance=product,data=req.data)


            if serializer.is_valid():
                serializer.save()

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productDelete(APIView):
    # only if the user created the data is allowed to delete
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def delete(self, req, pk):
        if req.method == "DELETE":

            product = get_object_or_404(Product,id=pk)
            # check if user have permission to delete the data
            self.check_object_permissions(req, product)
            product.delete()

            return Response(data={"success":f"product was successfully deleted"},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
