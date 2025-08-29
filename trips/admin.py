from django.contrib import admin
from .models import TravelOption

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('type', 'source', 'destination', 'departure', 'price', 'available_seats')
    list_filter = ('type', 'source', 'destination')
    search_fields = ('source', 'destination')