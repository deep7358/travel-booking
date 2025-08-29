from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'travel_option', 'seats', 'total_price', 'status', 'booking_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'travel_option__source', 'travel_option__destination')