from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.trip_list, name='list'),
    path('<int:pk>/', views.trip_detail, name='detail'),
]
