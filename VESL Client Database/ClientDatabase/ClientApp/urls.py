from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'Clients', views.ClientViewSet)
router.register(r'Facilities', views.FacilityViewSet)
router.register(r'Contacts', views.ContactViewSet)
router.register(r'Equipment', views.EquipmentViewSet)
router.register(r'Services', views.ServicesViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("listclients/", views.list_client_view, name="Clients"),
    path("api/", include(router.urls), name='api'),
]