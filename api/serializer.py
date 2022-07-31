from rest_framework import serializers
from .models import category, book, product
from .serializers import categoryserializer, bookserializer, productserializer

class categoryserializer(serializers.Modelserializer):
    class Meta:
        model = category
        Field = ('__all__')

class bookserializer(serializers.Modelserializer):
    class Meta:
        model = book
        Field = ('__all__')

class productserializer(serializers.Modelserializer):
    class Meta:
        model = product
        Field = ('__all__')


      