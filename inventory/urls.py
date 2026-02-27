from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'rentals', views.RentalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='inventory-index'),
]
