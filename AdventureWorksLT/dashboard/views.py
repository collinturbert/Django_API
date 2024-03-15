from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
def index(request):
    return HttpResponse("You have to start somewhere!")

def list_cust_view(request):
    data = models.Customer.objects.all()
    context = {"Customers":data}
    return render(request, 'list_cust.html', context)

class CustViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer