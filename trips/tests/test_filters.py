from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from trips.models import TravelOption

class TripFilterTests(TestCase):
    def setUp(self):
        TravelOption.objects.create(type='Flight', source='X', destination='Y',
            departure=timezone.now()+timedelta(days=1), price=100, available_seats=5)
        TravelOption.objects.create(type='Train', source='X', destination='Z',
            departure=timezone.now()+timedelta(days=2), price=50, available_seats=20)

    def test_type_filter(self):
        qs = TravelOption.objects.filter(type='Flight')
        self.assertEqual(qs.count(), 1)
