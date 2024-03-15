from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustViewSet)

urlpatterns = [
    path("message", views.index, name="index"),
    path("listcust/", views.list_cust_view, name="customers"),
    path("api/", include(router.urls), name='api'),
]