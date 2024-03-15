from django.db import models

# Create your models here.
class Customer(models.Model):
    FirstName = models.CharField(db_column = 'FirstName', max_length = 50)
    LastName = models.CharField(db_column = 'LastName', max_length = 50)
    
    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return (self.FirstName + "" + self.LastName)