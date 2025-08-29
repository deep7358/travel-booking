from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from trips.models import TravelOption
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta

class BookingFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('alice', 'a@example.com', 'pass12345')
        self.trip = TravelOption.objects.create(
            type='Bus', source='CityA', destination='CityB',
            departure=timezone.now()+timedelta(days=1),
            price=Decimal('100.00'), available_seats=10
        )

    def test_booking_reduces_seats(self):
        self.client.login(username='alice', password='pass12345')
        url = reverse('bookings:create', args=[self.trip.pk])
        resp = self.client.post(url, {'seats': 3}, follow=True)
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.available_seats, 7)

    def test_cannot_overbook(self):
        self.client.login(username='alice', password='pass12345')
        url = reverse('bookings:create', args=[self.trip.pk])
        resp = self.client.post(url, {'seats': 999}, follow=True)
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.available_seats, 10)
