from os import name
from django.core.checks import messages
import travels
from travels.models import Destination
from django.shortcuts import render
from .models import Destination, Traveler, Contact
from django.http import HttpResponse
# Create your views here.
def index(request):

    dests = Destination.objects.all()
    travelers = Traveler.objects.all()
    

    return render(request,'travels/index.html', {'dests': dests, 'travelers': travelers})
