# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Address
 
# Create a model serializer
class AddressSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Address
        fields = '__all__'