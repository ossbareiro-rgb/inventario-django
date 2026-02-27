from django.db import models


class ItemType(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    STATE_CHOICES = [
        ('available', 'Disponible'),
        ('rented', 'Alquilado'),
        ('sold', 'Vendido'),
        ('reserved', 'Reservado'),
        ('unavailable', 'No disponible'),
    ]

    item_type = models.ForeignKey(ItemType, on_delete=models.PROTECT, related_name='items')
    code = models.CharField(max_length=64, blank=True, help_text='Código o referencia')
    size = models.CharField(max_length=32, blank=True)
    color = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='available')
    date_added = models.DateField(auto_now_add=True)
    out_of_service = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.item_type.name} ({self.code or self.pk})"


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()


class Measurement(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='measurements')
    chest = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    waist = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    hips = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sleeve_length = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    trouser_length = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    shoulders = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    other = models.TextField(blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medidas de {self.client} ({self.recorded_at.date()})"


class Rental(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='rentals')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='rentals')
    date_rented = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Alquiler: {self.item} -> {self.client} ({self.date_rented})"
