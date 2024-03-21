import uuid
from django.db import models
from datetime import datetime

class ClientTable(models.Model):
    ClientID = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                unique=True, editable=False)
    CompanyName = models.CharField(max_length = 100)
    Address = models.CharField(max_length=60)
    State = models.CharField(max_length = 25)
    City = models.CharField(max_length=60)
    Zip = models.IntegerField()
    Phone = models.CharField(max_length=45, blank=True)
    ModifiedDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.CompanyName
    
    class Meta:
        db_table = 'Client'


class ServicesTable(models.Model):
    SERVICES_CHOICES = [
        ("24-7", "Twenty-Four Seven"),
        ("PS", "Partial Service"),
        ("1T", "One Time Service"),
    ]
    ServiceID = models.AutoField(primary_key=True)
    Client = models.ForeignKey(ClientTable, related_name = "Services", on_delete = models.CASCADE, null=True)
    ServiceType = models.CharField(max_length=4, choices=SERVICES_CHOICES)
    ModifiedDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Service ID: {self.ServiceID}, Client Name: {self.Client.CompanyName}, Service: {self.ServiceType}"
    
    class Meta:
        db_table = 'Services'

class FacilityTable(models.Model):
    FACILITY_TYPE = [
        ("A", "Food"),
        ("B", "Chemical"),
        ("C", "Textile"),
        ("D", "Web-Converting"),
    ]
    FacilityID = models.AutoField(primary_key=True)
    Client = models.ForeignKey(ClientTable, related_name="Facilities", on_delete = models.CASCADE, null=True)
    FacilityName = models.CharField(max_length = 100)
    FacilityType = models.CharField(max_length=1, choices=FACILITY_TYPE)
    Address = models.CharField(max_length=60)
    City = models.CharField(max_length=60)
    Zip = models.IntegerField()
    Phone = models.CharField(max_length=45, blank=True)
    ModifiedDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Facility Name: {self.FacilityName}"
    
    class Meta:
        db_table = 'Facilities'


class ContactTable(models.Model):
    ContactID = models.AutoField(primary_key=True)
    Client = models.ForeignKey(ClientTable, related_name="Contacts", on_delete = models.CASCADE, null=True)
    Facility = models.ForeignKey(FacilityTable, related_name="Contacts", on_delete = models.CASCADE, null=True)
    ClientPrimary = models.BooleanField(default = False)
    FacilityPrimary = models.BooleanField(default = False)
    Title = models.CharField(max_length=8, blank=True, null=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Phone = models.CharField(max_length=25, blank=True, null=True)
    VESLContact = models.CharField(max_length=256, blank=True, null=True)
    passwordhash = models.CharField(max_length=128)
    passwordsalt = models.CharField(max_length=10)
    ModifiedDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"""{self.FirstName} {self.LastName} with {self.Client.CompanyName}"""
    
    class Meta:
        db_table = 'Contacts'


class EquipmentTable(models.Model):
    EquipmentID = models.AutoField(primary_key=True)
    Client = models.ForeignKey(ClientTable, related_name="Equipment", on_delete = models.CASCADE, null=True)
    Facility = models.ForeignKey(FacilityTable, related_name="Equipment", on_delete = models.CASCADE, null=True)
    EquipmentName = models.CharField(max_length=50)
    SerialNum = models.IntegerField()
    IoT = models.BooleanField()
    IoTAddress = models.CharField(max_length = 120)
    Modeled = models.BooleanField()
    ModifiedDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"""Equipment ID: {self.EquipmentID}, 
                Equipment Name: {self.EquipmentName},
                Client: {self.Client.CompanyName},
                Facility: {self.Facility.FacilityName}"""
    
    class Meta:
        db_table = 'Equipment'