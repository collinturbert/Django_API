from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from . import models
from . import serializers

def index(request):
    return HttpResponse("Welcome to the VESL Client API!")

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def list_client_view(request):
    data = models.ClientTable.objects.all()
    context = {"Clients":data}
    return render(request, 'list_client.html', context)

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.ClientTable.objects.all()
    serializer_class = serializers.ClientSerializer

class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.ContactTable.objects.all()
    serializer_class = serializers.ContactSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.EquipmentTable.objects.all()
    serializer_class = serializers.EquipmentSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.FacilityTable.objects.all()
    serializer_class = serializers.FacilitySerializer

class ServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.ServicesTable.objects.all()
    serializer_class = serializers.ServicesSerializer