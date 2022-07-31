from django.shortcuts import render
from rest_framework import generics
from .serializer import categoryserializer, bookserializer, productserializer
#from rest_framework.view import APIView

# Create your views here.

class categorylist(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = categoryserializer

class categorydetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = category.objects.all()
    serializer_class = categoryserializer   

class booklist(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class = bookserializer

class bookdetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = book.objects.all()
    serializer_class = categoryserializer   

class productlist(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer

class productdetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = product.objects.all()
    serializer_class = productserializer   

