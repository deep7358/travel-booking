from django.db import models
from django.contrib.auth.models import User
from trips.models import TravelOption
from django.utils import timezone

class Booking(models.Model):
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'
    STATUS_CHOICES = [(CONFIRMED, 'Confirmed'), (CANCELLED, 'Cancelled')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE, related_name='bookings')
    seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    booking_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CONFIRMED)

    def __str__(self):
        return f"Booking #{self.pk} - {self.user} - {self.travel_option}"

    class Meta:
        ordering = ['-booking_date']