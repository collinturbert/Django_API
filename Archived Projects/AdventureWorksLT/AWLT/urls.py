from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listcust/",views.listCustomerPageView, name = "Customers")
]