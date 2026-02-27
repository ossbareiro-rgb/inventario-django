from django.contrib import admin
from . import models


@admin.register(models.ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_type', 'size', 'state', 'out_of_service')
    list_filter = ('item_type', 'state', 'out_of_service')
    search_fields = ('code',)
    actions = ['mark_available', 'mark_unavailable']

    def mark_available(self, request, queryset):
        queryset.update(state='available', out_of_service=False)
    mark_available.short_description = 'Marcar como disponible'

    def mark_unavailable(self, request, queryset):
        queryset.update(state='unavailable', out_of_service=True)
    mark_unavailable.short_description = 'Marcar como no disponible'


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'phone', 'email')


@admin.register(models.Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('client', 'recorded_at')
    search_fields = ('client__first_name', 'client__last_name')


@admin.register(models.Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('item', 'client', 'date_rented', 'expected_return_date', 'actual_return_date', 'paid')
    list_filter = ('paid',)
    search_fields = ('item__code', 'client__first_name', 'client__last_name')
