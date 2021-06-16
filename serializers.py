from rest_framework import serializers  #importing serializer from rest framework
from .models import Product             #importing Product model

"""
    It help us to serializer the data from models Product
    serializer help us to convert the data into json format
    and tyo take input in json format !!

    ProdtctSerializer : serializer for Product
"""

# This is the serializer for the  Model Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'
