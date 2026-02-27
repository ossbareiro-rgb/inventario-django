from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models, serializers


def index(request):
    items = models.Item.objects.all()[:20]
    return render(request, 'inventory/index.html', {'items': items})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RentalViewSet(viewsets.ModelViewSet):
    queryset = models.Rental.objects.all()
    serializer_class = serializers.RentalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
