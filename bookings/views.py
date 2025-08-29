from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from decimal import Decimal

from trips.models import TravelOption
from .models import Booking
from .forms import BookingForm

@login_required
@transaction.atomic
def create_booking(request, trip_id):
    trip = get_object_or_404(TravelOption, pk=trip_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats']
            trip = TravelOption.objects.select_for_update().get(pk=trip_id)
            if seats <= 0:
                messages.error(request, "Seats must be positive.")
            elif seats > trip.available_seats:
                messages.error(request, "Not enough seats available.")
            else:
                total_price = Decimal(seats) * trip.price
                Booking.objects.create(
                    user=request.user,
                    travel_option=trip,
                    seats=seats,
                    total_price=total_price,
                    status=Booking.CONFIRMED
                )
                trip.available_seats -= seats
                trip.save()
                messages.success(request, "Booking confirmed.")
                return redirect('bookings:mine')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form, 'trip': trip})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('travel_option')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
@transaction.atomic
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status == Booking.CANCELLED:
        return redirect('bookings:mine')
    if request.method == 'POST':
        booking.status = Booking.CANCELLED
        booking.save()
        trip = booking.travel_option
        trip = TravelOption.objects.select_for_update().get(pk=trip.pk)
        trip.available_seats += booking.seats
        trip.save()
        return redirect('bookings:mine')
    return render(request, 'bookings/confirm_cancel.html', {'booking': booking})