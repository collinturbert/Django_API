from django.db import models

class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    namestyle = models.BooleanField(db_column='NameStyle')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=8, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=10, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    salesperson = models.CharField(db_column='SalesPerson', max_length=256, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=128)  # Field name made lowercase.
    passwordsalt = models.CharField(db_column='PasswordSalt', max_length=10)  # Field name made lowercase.
    #rowguid = models.CharField(db_column='rowguid', max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    def __str__(self):
        return {'first_name': self.firstname, 'last_name': self.lastname}

    class Meta:
        db_table = 'SalesLT].[Customer'