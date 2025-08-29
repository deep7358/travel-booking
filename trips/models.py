from django.db import models

class TravelOption(models.Model):
    FLIGHT = 'Flight'
    TRAIN = 'Train'
    BUS = 'Bus'
    TYPE_CHOICES = [
        (FLIGHT, 'Flight'),
        (TRAIN, 'Train'),
        (BUS, 'Bus'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['departure']

    def __str__(self):
        return f"{self.type} {self.source}->{self.destination} @ {self.departure:%Y-%m-%d %H:%M}"