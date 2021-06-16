import travels
from travels.models import Destination
from django.shortcuts import render
from .models import Destination, Traveler

# Create your views here.
def index(request):

    dests = Destination.objects.all()
    travelers = Traveler.objects.all()

    return render(request,'travels/index.html', {'dests': dests, 'travelers': travelers})