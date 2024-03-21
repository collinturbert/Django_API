from rest_framework import serializers
from . import models

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServicesTable
        fields = ["ServiceID", "Client", "ServiceType", 
                  "ModifiedDate"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactTable
        fields = ["ContactID", "Client", "Facility", "ClientPrimary",
                  "FacilityPrimary", "Title", "FirstName", 
                  "LastName", "Email", "Phone", "VESLContact", 
                  "passwordhash", "passwordsalt", "ModifiedDate"]


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EquipmentTable
        fields = ["EquipmentID", "Client", "Facility", 
                  "EquipmentName", "SerialNum", "IoT", 
                  "IoTAddress", "Modeled", "ModifiedDate"]
        

class FacilitySerializer(serializers.ModelSerializer):
    Contacts = ContactSerializer(many=True, read_only=True)
    Equipment = EquipmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.FacilityTable
        fields = ["FacilityID", "Client", "FacilityName", 
                 "FacilityType", "Contacts", "Address", 
                  "City", "Zip", "Phone", "Equipment",
                  "ModifiedDate"]


class ClientSerializer(serializers.ModelSerializer):
    Services = ServicesSerializer(many=True, read_only=True)
    Contacts = ContactSerializer(many=True, read_only=True)
    Facilities = FacilitySerializer(many=True, read_only=True)

    class Meta:
        model = models.ClientTable
        fields = ["ClientID", "CompanyName", "Services",
                  "Contacts", "Facilities", "Address", "State", 
                  "City", "Zip", "Phone", "ModifiedDate"]