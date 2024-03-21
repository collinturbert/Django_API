from django.contrib import admin
from . import models

admin.site.register(models.ClientTable)
admin.site.register(models.ContactTable)
admin.site.register(models.EquipmentTable)
admin.site.register(models.FacilityTable)
admin.site.register(models.ServicesTable)