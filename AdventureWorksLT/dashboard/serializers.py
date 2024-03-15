from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ["customerid", "namestyle", "title", "firstname", 
                "middlename", "lastname", "suffix", "companyname", 
                "salesperson", "emailaddress", "phone", "passwordhash", 
                "passwordsalt", "modifieddate"]