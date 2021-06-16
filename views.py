from django.shortcuts import render
from .models import Product
from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListProduct(APIView):
    """
         this get function will display all the product that are available to the data base
    """
    def get(self,request):
        data=Product.objects.all()
        serializer = ProductSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class DetailProduct(APIView):
    """docstring for DetailView"""
    # the below function will check where the object with following primary key
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)                                       # if there is object it will get that object
        except Product.DoesNotExist:
            raise Http404                                                           # raise the http 404 not found
    def get(self,request,pk):
        product=self.get_object(pk)                                                 #initalizing product
        serializer = ProductSerializer(product)                                     #initalizing serializer for product
        return Response(serializer.data)                                            #returning serializer data f
    def put(self,request,pk):
        product = self.get_object(pk)                                               #initalizing product
        serializer= ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class DetailProductByName(APIView):
    def get_object(self,name):
        try:
            return Product.objects.filter(name=name)
        except Product.DoesNotExist:
            raise Http404
    def get(self,request,name):
        product = self.get_object(name)
        serializer= ProductSerializer(product,many=True)
        return Response(serializer.data)
    def put(self,request,name):
        product = self.get_object(name)
        serializer = ProductSerializer(product,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, name):
        product = Product.get_object(name)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


