from rest_framework import serializers
from . import models


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemType
        fields = ['id', 'name', 'description']


class ItemSerializer(serializers.ModelSerializer):
    item_type = ItemTypeSerializer(read_only=True)
    item_type_id = serializers.PrimaryKeyRelatedField(queryset=models.ItemType.objects.all(), source='item_type', write_only=True)

    class Meta:
        model = models.Item
        fields = ['id', 'item_type', 'item_type_id', 'code', 'size', 'color', 'state', 'date_added', 'out_of_service', 'notes']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'notes']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measurement
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=models.Item.objects.all(), source='item', write_only=True)
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(queryset=models.Client.objects.all(), source='client', write_only=True)

    class Meta:
        model = models.Rental
        fields = ['id', 'item', 'item_id', 'client', 'client_id', 'date_rented', 'expected_return_date', 'actual_return_date', 'price', 'paid', 'notes']
