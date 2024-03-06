# basic URL Configurations
from django.urls import include, path

# import routers
from rest_framework import router
 
# import everything from views
from . import views
 
# specify URL Path for rest_framework
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/address/', views.address_list, name = 'get_address'),
    path('api/address/<int:pk>/', views.address_update, name = 'update_address'),
]