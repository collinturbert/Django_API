from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def index(request):
    return HttpResponse("You have to start somewhere!")

def listCustomerPageView(request):
    data = Customer.objects.all()
    context = {"Customers":data}
    return render(request, "listcust.html", context)