from django.shortcuts import render, get_object_or_404
from django.utils.timezone import make_aware
from datetime import datetime, time
from .models import TravelOption
from .forms import TripFilterForm

def trip_list(request):
    qs = TravelOption.objects.all()
    form = TripFilterForm(request.GET or None)
    if form.is_valid():
        t = form.cleaned_data.get('type')
        s = form.cleaned_data.get('source')
        d = form.cleaned_data.get('destination')
        date = form.cleaned_data.get('date')
        if t:
            qs = qs.filter(type=t)
        if s:
            qs = qs.filter(source__icontains=s)
        if d:
            qs = qs.filter(destination__icontains=d)
        if date:
            start = make_aware(datetime.combine(date, time.min))
            end = make_aware(datetime.combine(date, time.max))
            qs = qs.filter(departure__range=(start, end))
    return render(request, 'trips/trip_list.html', {'form': form, 'trips': qs})

def trip_detail(request, pk):
    trip = get_object_or_404(TravelOption, pk=pk)
    return render(request, 'trips/trip_detail.html', {'trip': trip})