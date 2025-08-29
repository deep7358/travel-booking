from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('create/<int:trip_id>/', views.create_booking, name='create'),
    path('mine/', views.my_bookings, name='mine'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel'),
]
